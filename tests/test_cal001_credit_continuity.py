from __future__ import annotations

import json
import subprocess
from pathlib import Path

from app.ai_video_pipeline.execution.dreamina_evidence import (
    validate_post_submit_credit_reconciliation,
    validate_pre_submit_credit_continuity,
)


ROOT = Path(__file__).resolve().parents[1]
STARTING_CHECKPOINT = "7c86367a3d7ca17bb63e8ad148144b3075f4dab7"
STATE_PATH = (
    "experiments/CAL-001/execution_state/"
    "CAL001_P3C_remaining_77_resumable_execution_state_contract.json"
)


def test_01_positive_nonspend_drift_passes_without_scope_enlargement() -> None:
    result = validate_pre_submit_credit_continuity(
        prior_observed_balance=5957,
        current_observed_balance=6045,
        required_dynamic_threshold=5950,
        intervening_authorized_CAL001_submit_count=0,
    )

    assert result.passed is True
    assert result.classification == "positive_nonspend_credit_drift"
    assert result.current_balance_numeric == 6045
    assert result.threshold_passed is True
    assert result.drift_amount == 88
    assert result.drift_direction == "positive"
    assert result.scope_or_budget_enlarged is False
    assert result.stop_condition is None


def test_02_below_threshold_current_balance_stops() -> None:
    result = validate_pre_submit_credit_continuity(
        prior_observed_balance=5957,
        current_observed_balance=5949,
        required_dynamic_threshold=5950,
        intervening_authorized_CAL001_submit_count=0,
    )

    assert result.passed is False
    assert result.classification == "below_dynamic_credit_threshold"
    assert result.threshold_passed is False
    assert result.stop_condition


def test_03_unexplained_negative_drift_without_submit_stops() -> None:
    result = validate_pre_submit_credit_continuity(
        prior_observed_balance=6045,
        current_observed_balance=6035,
        required_dynamic_threshold=5950,
        intervening_authorized_CAL001_submit_count=0,
    )

    assert result.passed is False
    assert result.classification == "unexplained_negative_credit_drift"
    assert result.drift_amount == -10
    assert result.drift_direction == "negative"
    assert result.stop_condition


def test_04_no_drift_with_threshold_passes() -> None:
    result = validate_pre_submit_credit_continuity(
        prior_observed_balance=6045,
        current_observed_balance=6045,
        required_dynamic_threshold=5950,
        intervening_authorized_CAL001_submit_count=0,
    )

    assert result.passed is True
    assert result.classification == "no_pre_submit_credit_drift"
    assert result.drift_amount == 0
    assert result.drift_direction == "none"


def test_05_exact_post_submit_delta_and_provider_count_pass() -> None:
    result = validate_post_submit_credit_reconciliation(
        immediate_pre_submit_balance=6045,
        immediate_post_submit_balance=5975,
        provider_credit_count=70,
    )

    assert result.passed is True
    assert result.classification == "exact_70_credit_reconciliation"
    assert result.observed_credit_delta == 70
    assert result.provider_credit_count_numeric == 70
    assert result.stop_condition is None


def test_06_non_70_post_submit_delta_stops() -> None:
    result = validate_post_submit_credit_reconciliation(
        immediate_pre_submit_balance=6045,
        immediate_post_submit_balance=5976,
        provider_credit_count=70,
    )

    assert result.passed is False
    assert result.classification == "post_submit_credit_delta_not_70"
    assert result.stop_condition


def test_07_absent_provider_credit_count_stops() -> None:
    result = validate_post_submit_credit_reconciliation(
        immediate_pre_submit_balance=6045,
        immediate_post_submit_balance=5975,
        provider_credit_count=None,
    )

    assert result.passed is False
    assert result.classification == "provider_credit_count_absent"


def test_08_nonnumeric_provider_credit_count_stops() -> None:
    result = validate_post_submit_credit_reconciliation(
        immediate_pre_submit_balance=6045,
        immediate_post_submit_balance=5975,
        provider_credit_count="ambiguous",
    )

    assert result.passed is False
    assert result.classification == "provider_credit_count_nonnumeric"


def test_09_provider_credit_count_other_than_70_stops() -> None:
    result = validate_post_submit_credit_reconciliation(
        immediate_pre_submit_balance=6045,
        immediate_post_submit_balance=5975,
        provider_credit_count=69,
    )

    assert result.passed is False
    assert result.classification == "provider_credit_count_not_70"


def test_10_positive_drift_does_not_mutate_authorized_limits() -> None:
    authorized_limits = {
        "remaining_fixed_task_count": 77,
        "remaining_credit_budget_max": 5390,
        "wave_scope": "W01_ONLY",
    }
    before = authorized_limits.copy()

    result = validate_pre_submit_credit_continuity(
        prior_observed_balance=5957,
        current_observed_balance=6045,
        required_dynamic_threshold=5950,
        intervening_authorized_CAL001_submit_count=0,
    )

    assert result.passed is True
    assert result.scope_or_budget_enlarged is False
    assert authorized_limits == before


def test_11_historical_f01_submit_attempt_count_was_zero_before_reopening() -> None:
    completed = subprocess.run(
        ["git", "show", f"{STARTING_CHECKPOINT}:{STATE_PATH}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    historical_state = json.loads(completed.stdout)
    w01 = next(
        wave for wave in historical_state["initial_waves"] if wave["wave_id"] == "W01"
    )
    f01 = next(
        task
        for task in w01["tasks"]
        if task["experiment_id"] == "CAL001-F01-P1-R1"
    )

    assert historical_state["activation_state"] == "STOPPED_AUTHORITY_CLOSED"
    assert w01["wave_state"] == "stopped"
    assert f01["task_state"] == "stopped_anomaly"
    assert f01["submit_attempt_count"] == 0
    assert f01["submit_id"] is None
