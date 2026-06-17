# A-SC-TEMPLE-COURTYARD-003 Readiness Review

Task: A-SC-TEMPLE-COURTYARD-003

Target asset: A-SC-TEMPLE-COURTYARD-003_main_hall_frontal_axis_stage

Status: historical_failed_composition_example

Needs generation: false

Locked: false

Task type: image2image

Model version: 4.7

Ratio: 16:9

Resolution type: 2k

## Package Purpose

Viewpoint-correction scene anchor for SHOT-02 that attempted to redirect the A-SC-002 oblique composition. The manual review found it insufficiently frontal and still too tied to side-facing composition.

## Primary Input Reference

- productions/chi_yan_tian_qiong/runs/live/20260616_141522_A-SC-TEMPLE-COURTYARD-002/output/A-SC-TEMPLE-COURTYARD-002_main_hall_front_combat_stage.png

## Required Visual Checks After Generation

- Character-free scene only
- No human figures or silhouettes
- No monks, visitors, guards, umbrella-shaped human figures, statues, or wall paintings that read as people
- Main hall is frontal and central
- Main hall door, steps, railings, and central axis are clear
- Mid-courtyard combat stage is usable
- Left and right entry/movement space preserved
- Foreground wet stone reflections present but not dominant
- Rainy ancient temple continuity preserved
- No unrelated location drift
- No text or watermark

## Failure result

- Manual review outcome: failed_composition_example
- Reason: A-SC-TEMPLE-COURTYARD-003 retained obvious oblique viewing bias and did not deliver the required true frontal-axis correction.
- Status effect: marked as historical failed composition example; do not use this as active scene-anchor candidate.

## Package Files

- Manual prompt: productions/chi_yan_tian_qiong/prompts/manual_A-SC-TEMPLE-COURTYARD-003_main_hall_frontal_axis_stage_prompt.txt
- Prompt JSON: productions/chi_yan_tian_qiong/prompts/production_scene_asset_prompt_A-SC-TEMPLE-COURTYARD-003.json
- Manifest: productions/chi_yan_tian_qiong/manifests/production_image2image_A-SC-TEMPLE-COURTYARD-003.csv

## Decision

historical_failed_composition_example
