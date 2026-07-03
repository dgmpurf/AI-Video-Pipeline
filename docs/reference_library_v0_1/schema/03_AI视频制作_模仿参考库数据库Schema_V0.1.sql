-- AI视频制作_模仿参考库数据库Schema_V0.1
-- Purpose: local-first SQLite schema for an AI video mimic/reference library.
-- Scope: raw clips, reference segments, bilingual controlled tags, FTS5 search,
--        safety/usage gates, attempts, feedback, context-aware ranking, and future embeddings.
-- Important: video files are stored on disk. SQLite stores paths, metadata, tags, search text,
--            safety state, and usage feedback. Reference videos are not final assets.

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;

-- -----------------------------------------------------------------------------
-- 0. Schema metadata
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS schema_migrations (
    version TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    applied_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT
);

INSERT OR IGNORE INTO schema_migrations(version, name, notes)
VALUES ('0.1.0', 'mimic_reference_library_initial_schema', 'Initial V0.1 schema for local AI video mimic reference library.');

CREATE TABLE IF NOT EXISTS library_settings (
    setting_key TEXT PRIMARY KEY,
    setting_value TEXT,
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT
);

INSERT OR IGNORE INTO library_settings(setting_key, setting_value, notes)
VALUES
('library_version', '0.1.0', 'Schema version.'),
('default_usage_class', 'offline_grammar_only', 'External clips default to offline grammar.'),
('default_active_input_allowed', '0', 'Active input is false until reviewed.'),
('media_in_git_allowed', '0', 'Original/full reference videos should not be committed to Git.');

-- -----------------------------------------------------------------------------
-- 1. Controlled bilingual tag dictionary
-- Matches 02_AI视频制作_模仿参考库标签字典_V0.1.csv columns.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY,
    tag_id TEXT NOT NULL UNIQUE,
    tag_key TEXT NOT NULL UNIQUE,
    zh_name TEXT,
    en_name TEXT,
    category TEXT NOT NULL,
    parent_tag_key TEXT,
    level TEXT NOT NULL, -- L1 / L2 / L3
    aliases_zh TEXT,
    aliases_en TEXT,
    use_for_exact_filter INTEGER NOT NULL DEFAULT 1,
    use_for_fulltext INTEGER NOT NULL DEFAULT 1,
    use_for_semantic INTEGER NOT NULL DEFAULT 0,
    use_for_weighting INTEGER NOT NULL DEFAULT 1,
    default_usage_class TEXT DEFAULT 'offline_grammar_only',
    default_active_input_allowed INTEGER NOT NULL DEFAULT 0,
    default_reference_role TEXT,
    risk_level TEXT DEFAULT 'none',
    description_zh TEXT,
    description_en TEXT,
    examples TEXT,
    do_not_use_for TEXT,
    source_basis TEXT,
    status TEXT NOT NULL DEFAULT 'active',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY(parent_tag_key) REFERENCES tags(tag_key)
);

CREATE TABLE IF NOT EXISTS tag_aliases (
    alias_id INTEGER PRIMARY KEY,
    tag_key TEXT NOT NULL,
    alias TEXT NOT NULL,
    lang TEXT, -- zh / en / mixed
    source TEXT DEFAULT 'tag_dictionary',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE(tag_key, alias, lang),
    FOREIGN KEY(tag_key) REFERENCES tags(tag_key) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_tags_category_level ON tags(category, level);
CREATE INDEX IF NOT EXISTS idx_tags_parent ON tags(parent_tag_key);
CREATE INDEX IF NOT EXISTS idx_tag_aliases_alias ON tag_aliases(alias);

-- -----------------------------------------------------------------------------
-- 2. Raw clips: physical source files and top-level rights/provenance state
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS raw_clips (
    id INTEGER PRIMARY KEY,
    raw_clip_id TEXT NOT NULL UNIQUE,
    title TEXT,
    source_type TEXT NOT NULL DEFAULT 'unknown', -- film/tv/gameplay/anime/mocap/ae_pr/self_shot/tutorial/unknown...
    source_name TEXT,
    source_url TEXT,
    source_timecode TEXT,
    creator TEXT,
    credit_line TEXT,
    copyright_notice TEXT,
    digital_source_type TEXT,
    local_path TEXT NOT NULL UNIQUE,
    file_sha256 TEXT,
    file_size_bytes INTEGER,
    format TEXT,
    video_codec TEXT,
    audio_codec TEXT,
    has_audio INTEGER NOT NULL DEFAULT 0 CHECK(has_audio IN (0,1)),
    duration_ms INTEGER,
    width INTEGER,
    height INTEGER,
    fps REAL,
    aspect_ratio TEXT,
    language TEXT,
    rights_status TEXT NOT NULL DEFAULT 'unknown', -- unknown/public_reference_only/licensed/self_owned/client_owned/restricted/prohibited
    usage_class TEXT NOT NULL DEFAULT 'offline_grammar_only', -- offline_grammar_only/prompt_influence_allowed/review_standard_only/active_input_allowed/do_not_use
    active_input_allowed INTEGER NOT NULL DEFAULT 0 CHECK(active_input_allowed IN (0,1)),
    prompt_influence_allowed INTEGER NOT NULL DEFAULT 1 CHECK(prompt_influence_allowed IN (0,1)),
    review_standard_only INTEGER NOT NULL DEFAULT 0 CHECK(review_standard_only IN (0,1)),
    offline_grammar_only INTEGER NOT NULL DEFAULT 1 CHECK(offline_grammar_only IN (0,1)),
    do_not_use INTEGER NOT NULL DEFAULT 0 CHECK(do_not_use IN (0,1)),
    human_review_required INTEGER NOT NULL DEFAULT 1 CHECK(human_review_required IN (0,1)),
    risk_level TEXT NOT NULL DEFAULT 'unknown', -- none/low/medium/high/block
    risk_tags_json TEXT,
    provenance_status TEXT DEFAULT 'unknown', -- known/partial/unknown/suspicious
    content_credentials_status TEXT DEFAULT 'absent', -- absent/present/verified/invalid
    ai_training_preference TEXT DEFAULT 'unknown', -- none/no_train/no_reference_use/unknown
    import_status TEXT NOT NULL DEFAULT 'imported', -- imported/probed/artifacts_done/triaged/rejected/error
    imported_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT,
    extra_json TEXT
);

CREATE INDEX IF NOT EXISTS idx_raw_clips_source_type ON raw_clips(source_type);
CREATE INDEX IF NOT EXISTS idx_raw_clips_rights_status ON raw_clips(rights_status);
CREATE INDEX IF NOT EXISTS idx_raw_clips_usage_class ON raw_clips(usage_class);
CREATE INDEX IF NOT EXISTS idx_raw_clips_active_input ON raw_clips(active_input_allowed, do_not_use);
CREATE INDEX IF NOT EXISTS idx_raw_clips_sha256 ON raw_clips(file_sha256);

-- -----------------------------------------------------------------------------
-- 3. Derived media artifacts: thumbnails, proxies, contact sheets, frames, waveform, JSON outputs
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS media_artifacts (
    artifact_id TEXT PRIMARY KEY,
    raw_clip_id TEXT NOT NULL,
    ref_id TEXT,
    artifact_type TEXT NOT NULL, -- poster/thumb/contact_sheet/keyframe/proxy/muted_proxy/waveform/asr_json/ocr_json/detection_json
    local_path TEXT NOT NULL,
    file_sha256 TEXT,
    timestamp_ms INTEGER,
    width INTEGER,
    height INTEGER,
    duration_ms INTEGER,
    created_by TEXT,
    status TEXT NOT NULL DEFAULT 'ready',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT,
    extra_json TEXT,
    FOREIGN KEY(raw_clip_id) REFERENCES raw_clips(raw_clip_id) ON DELETE CASCADE,
    FOREIGN KEY(ref_id) REFERENCES ref_segments(ref_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_media_artifacts_raw ON media_artifacts(raw_clip_id, artifact_type);
CREATE INDEX IF NOT EXISTS idx_media_artifacts_ref ON media_artifacts(ref_id, artifact_type);

-- -----------------------------------------------------------------------------
-- 4. Reference segments: primary search and reuse unit
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ref_segments (
    id INTEGER PRIMARY KEY,
    ref_id TEXT NOT NULL UNIQUE,
    raw_clip_id TEXT NOT NULL,
    title TEXT NOT NULL,
    summary TEXT,
    local_segment_path TEXT,
    thumb_path TEXT,
    contact_sheet_path TEXT,
    poster_path TEXT,
    start_ms INTEGER NOT NULL DEFAULT 0,
    end_ms INTEGER NOT NULL DEFAULT 0,
    duration_ms INTEGER NOT NULL DEFAULT 0,
    useful_window TEXT,
    primary_ref_type TEXT NOT NULL DEFAULT 'MIXED', -- ACTION/CAMERA/FX/EDIT/PERF/COMP/STYLE/ENV/SOUND/MOCAP/MIXED
    secondary_ref_types_json TEXT,
    source_type TEXT NOT NULL DEFAULT 'unknown',
    source_timecode TEXT,
    rights_status TEXT NOT NULL DEFAULT 'unknown',
    usage_class TEXT NOT NULL DEFAULT 'offline_grammar_only',
    active_input_allowed INTEGER NOT NULL DEFAULT 0 CHECK(active_input_allowed IN (0,1)),
    prompt_influence_allowed INTEGER NOT NULL DEFAULT 1 CHECK(prompt_influence_allowed IN (0,1)),
    review_standard_only INTEGER NOT NULL DEFAULT 0 CHECK(review_standard_only IN (0,1)),
    offline_grammar_only INTEGER NOT NULL DEFAULT 1 CHECK(offline_grammar_only IN (0,1)),
    do_not_use INTEGER NOT NULL DEFAULT 0 CHECK(do_not_use IN (0,1)),
    human_review_required INTEGER NOT NULL DEFAULT 1 CHECK(human_review_required IN (0,1)),
    risk_level TEXT NOT NULL DEFAULT 'unknown',
    risk_score REAL NOT NULL DEFAULT 0,
    risk_tags_json TEXT,
    contains_face INTEGER NOT NULL DEFAULT 0 CHECK(contains_face IN (0,1)),
    contains_voice INTEGER NOT NULL DEFAULT 0 CHECK(contains_voice IN (0,1)),
    contains_music INTEGER NOT NULL DEFAULT 0 CHECK(contains_music IN (0,1)),
    contains_logo INTEGER NOT NULL DEFAULT 0 CHECK(contains_logo IN (0,1)),
    contains_ui_hud INTEGER NOT NULL DEFAULT 0 CHECK(contains_ui_hud IN (0,1)),
    contains_watermark INTEGER NOT NULL DEFAULT 0 CHECK(contains_watermark IN (0,1)),
    contains_subtitles INTEGER NOT NULL DEFAULT 0 CHECK(contains_subtitles IN (0,1)),
    contains_text_overlay INTEGER NOT NULL DEFAULT 0 CHECK(contains_text_overlay IN (0,1)),
    fx_execution_mode TEXT, -- generate_inside_model/generate_plus_post/post_only/editing_reference_only/review_standard_only
    post_required INTEGER NOT NULL DEFAULT 0 CHECK(post_required IN (0,1)),
    model_generation_risk TEXT DEFAULT 'medium',
    prompt_suitability TEXT DEFAULT 'medium', -- high/medium/low/none
    prompt_words_zh TEXT,
    prompt_words_en TEXT,
    reference_duty TEXT,
    do_not_copy TEXT,
    review_criteria TEXT,
    post_plan TEXT,
    edit_timeline_note TEXT,
    fx_layer TEXT,
    sound_sync TEXT,
    cut_point_ms INTEGER,
    post_tool_suggestion TEXT,
    quality_score REAL NOT NULL DEFAULT 0,
    action_score REAL NOT NULL DEFAULT 0,
    camera_score REAL NOT NULL DEFAULT 0,
    fx_score REAL NOT NULL DEFAULT 0,
    edit_score REAL NOT NULL DEFAULT 0,
    similarity_score REAL NOT NULL DEFAULT 0,
    reuse_score REAL NOT NULL DEFAULT 0,
    success_count INTEGER NOT NULL DEFAULT 0,
    failure_count INTEGER NOT NULL DEFAULT 0,
    last_used_at TEXT,
    review_state TEXT NOT NULL DEFAULT 'raw', -- raw/triaged/useful/deep_tagged/prompt_ready/active_safe/offline_only/rejected
    status TEXT NOT NULL DEFAULT 'active', -- active/archived/rejected/deleted_stub
    tag_text TEXT,
    alias_text TEXT,
    risk_text TEXT,
    query_text TEXT,
    notes TEXT,
    extra_json TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    CHECK(end_ms >= start_ms),
    FOREIGN KEY(raw_clip_id) REFERENCES raw_clips(raw_clip_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_ref_segments_raw ON ref_segments(raw_clip_id);
CREATE INDEX IF NOT EXISTS idx_ref_segments_type ON ref_segments(primary_ref_type, source_type);
CREATE INDEX IF NOT EXISTS idx_ref_segments_usage ON ref_segments(usage_class, active_input_allowed, do_not_use);
CREATE INDEX IF NOT EXISTS idx_ref_segments_review_state ON ref_segments(review_state, status);
CREATE INDEX IF NOT EXISTS idx_ref_segments_fx_mode ON ref_segments(fx_execution_mode, prompt_suitability);
CREATE INDEX IF NOT EXISTS idx_ref_segments_risk ON ref_segments(risk_level, risk_score);
CREATE INDEX IF NOT EXISTS idx_ref_segments_time ON ref_segments(raw_clip_id, start_ms, end_ms);

-- -----------------------------------------------------------------------------
-- 5. Segment-tag mapping and AI suggestions
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS segment_tags (
    ref_id TEXT NOT NULL,
    tag_key TEXT NOT NULL,
    weight REAL NOT NULL DEFAULT 1.0,
    confidence REAL NOT NULL DEFAULT 1.0,
    source_method TEXT NOT NULL DEFAULT 'manual', -- manual/auto/rule/imported/agent_suggested
    confirmed INTEGER NOT NULL DEFAULT 1 CHECK(confirmed IN (0,1)),
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT,
    PRIMARY KEY(ref_id, tag_key),
    FOREIGN KEY(ref_id) REFERENCES ref_segments(ref_id) ON DELETE CASCADE,
    FOREIGN KEY(tag_key) REFERENCES tags(tag_key) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_segment_tags_tag ON segment_tags(tag_key, confirmed);
CREATE INDEX IF NOT EXISTS idx_segment_tags_ref ON segment_tags(ref_id);

CREATE TABLE IF NOT EXISTS auto_tag_suggestions (
    suggestion_id TEXT PRIMARY KEY,
    ref_id TEXT,
    raw_clip_id TEXT,
    tag_key TEXT NOT NULL,
    confidence REAL NOT NULL DEFAULT 0,
    source_engine TEXT NOT NULL, -- filename_rule/vlm/clip/ocr/asr/pose/manual_import
    rationale TEXT,
    status TEXT NOT NULL DEFAULT 'pending', -- pending/accepted/rejected/ignored
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    reviewed_at TEXT,
    FOREIGN KEY(ref_id) REFERENCES ref_segments(ref_id) ON DELETE CASCADE,
    FOREIGN KEY(raw_clip_id) REFERENCES raw_clips(raw_clip_id) ON DELETE CASCADE,
    FOREIGN KEY(tag_key) REFERENCES tags(tag_key) ON DELETE RESTRICT
);

-- -----------------------------------------------------------------------------
-- 6. Automatic annotations: OCR, ASR, face/pose/object detections, VLM captions
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS transcripts (
    transcript_id TEXT PRIMARY KEY,
    raw_clip_id TEXT NOT NULL,
    ref_id TEXT,
    start_ms INTEGER,
    end_ms INTEGER,
    text TEXT NOT NULL,
    language TEXT,
    source_engine TEXT, -- faster-whisper/whisper.cpp/whisperx/vosk/manual
    confidence REAL,
    status TEXT DEFAULT 'auto',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY(raw_clip_id) REFERENCES raw_clips(raw_clip_id) ON DELETE CASCADE,
    FOREIGN KEY(ref_id) REFERENCES ref_segments(ref_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_transcripts_raw ON transcripts(raw_clip_id, start_ms, end_ms);
CREATE INDEX IF NOT EXISTS idx_transcripts_ref ON transcripts(ref_id);

CREATE TABLE IF NOT EXISTS detections (
    detection_id TEXT PRIMARY KEY,
    raw_clip_id TEXT NOT NULL,
    ref_id TEXT,
    artifact_id TEXT,
    timestamp_ms INTEGER,
    detection_type TEXT NOT NULL, -- face/pose/object/logo/watermark/subtitle/ui/text/audio_event
    label TEXT,
    score REAL,
    bbox_json TEXT,
    value_json TEXT,
    source_engine TEXT,
    status TEXT DEFAULT 'auto',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY(raw_clip_id) REFERENCES raw_clips(raw_clip_id) ON DELETE CASCADE,
    FOREIGN KEY(ref_id) REFERENCES ref_segments(ref_id) ON DELETE CASCADE,
    FOREIGN KEY(artifact_id) REFERENCES media_artifacts(artifact_id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_detections_type ON detections(detection_type, label, score);
CREATE INDEX IF NOT EXISTS idx_detections_ref ON detections(ref_id, detection_type);
CREATE INDEX IF NOT EXISTS idx_detections_raw_time ON detections(raw_clip_id, timestamp_ms);

CREATE TABLE IF NOT EXISTS captions (
    caption_id TEXT PRIMARY KEY,
    raw_clip_id TEXT NOT NULL,
    ref_id TEXT,
    artifact_id TEXT,
    caption_text TEXT NOT NULL,
    caption_type TEXT DEFAULT 'vlm', -- vlm/human/ocr_summary/asr_summary
    source_engine TEXT,
    confidence REAL,
    status TEXT DEFAULT 'auto',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY(raw_clip_id) REFERENCES raw_clips(raw_clip_id) ON DELETE CASCADE,
    FOREIGN KEY(ref_id) REFERENCES ref_segments(ref_id) ON DELETE CASCADE,
    FOREIGN KEY(artifact_id) REFERENCES media_artifacts(artifact_id) ON DELETE SET NULL
);

-- -----------------------------------------------------------------------------
-- 7. Embeddings: optional future semantic/vector retrieval
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS embeddings (
    embedding_id TEXT PRIMARY KEY,
    raw_clip_id TEXT,
    ref_id TEXT,
    artifact_id TEXT,
    modality TEXT NOT NULL, -- visual_frame/visual_pooled/text/audio/pose
    scope TEXT NOT NULL DEFAULT 'segment', -- raw_clip/segment/frame/transcript
    model_name TEXT NOT NULL,
    model_version TEXT,
    dim INTEGER NOT NULL,
    vector_blob BLOB, -- optional local BLOB for small experiments
    external_store_ref TEXT, -- FAISS/Qdrant/sqlite-vec row id/file path/etc.
    distance_metric TEXT DEFAULT 'cosine',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT,
    FOREIGN KEY(raw_clip_id) REFERENCES raw_clips(raw_clip_id) ON DELETE CASCADE,
    FOREIGN KEY(ref_id) REFERENCES ref_segments(ref_id) ON DELETE CASCADE,
    FOREIGN KEY(artifact_id) REFERENCES media_artifacts(artifact_id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_embeddings_ref ON embeddings(ref_id, modality, model_name);
CREATE INDEX IF NOT EXISTS idx_embeddings_raw ON embeddings(raw_clip_id, modality, model_name);

-- -----------------------------------------------------------------------------
-- 8. Scene/script context for context-aware ranking
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS scene_contexts (
    id INTEGER PRIMARY KEY,
    context_id TEXT NOT NULL UNIQUE,
    strict_context_key TEXT NOT NULL,
    soft_context_key TEXT NOT NULL,
    coarse_context_key TEXT NOT NULL,
    project_name TEXT,
    project_type TEXT,
    scene_type TEXT,
    shot_id TEXT,
    shot_goal TEXT,
    primary_ref_type TEXT,
    action_need_text TEXT,
    camera_need_text TEXT,
    fx_need_text TEXT,
    environment_need_text TEXT,
    style_need_text TEXT,
    risk_mode TEXT,
    task_type TEXT,
    model_family TEXT,
    model_version TEXT,
    input_mode TEXT, -- offline_grammar/prompt_influence/review_standard/active_input
    context_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT
);

CREATE INDEX IF NOT EXISTS idx_contexts_keys ON scene_contexts(strict_context_key, soft_context_key, coarse_context_key);
CREATE INDEX IF NOT EXISTS idx_contexts_project_shot ON scene_contexts(project_name, shot_id);
CREATE INDEX IF NOT EXISTS idx_contexts_task_model ON scene_contexts(task_type, model_family);

-- -----------------------------------------------------------------------------
-- 9. Retrieval and generation attempts
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS retrieval_attempts (
    retrieval_id TEXT PRIMARY KEY,
    context_id TEXT,
    mode TEXT NOT NULL DEFAULT 'prompt_only', -- active_input/prompt_only/review_only/offline_grammar
    search_query TEXT,
    filters_json TEXT,
    candidate_ref_ids_json TEXT,
    selected_ref_ids_json TEXT,
    scoring_json TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT,
    FOREIGN KEY(context_id) REFERENCES scene_contexts(context_id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_retrieval_context ON retrieval_attempts(context_id, mode, created_at);

CREATE TABLE IF NOT EXISTS generation_attempts (
    attempt_id TEXT PRIMARY KEY,
    retrieval_id TEXT,
    context_id TEXT,
    project_name TEXT,
    shot_id TEXT,
    prompt_id TEXT,
    prompt_path TEXT,
    model_family TEXT,
    model_version TEXT,
    task_type TEXT,
    input_mode TEXT,
    selected_ref_ids_json TEXT,
    result_status TEXT, -- success/partial_success/failure/not_tested/unsafe_blocked
    success_type TEXT,
    failure_type TEXT,
    visual_score REAL,
    action_score REAL,
    camera_score REAL,
    fx_score REAL,
    identity_score REAL,
    output_path TEXT,
    review_artifact_path TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    reviewed_at TEXT,
    notes TEXT,
    FOREIGN KEY(retrieval_id) REFERENCES retrieval_attempts(retrieval_id) ON DELETE SET NULL,
    FOREIGN KEY(context_id) REFERENCES scene_contexts(context_id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_generation_context ON generation_attempts(context_id, task_type, model_family);
CREATE INDEX IF NOT EXISTS idx_generation_project_shot ON generation_attempts(project_name, shot_id, created_at);
CREATE INDEX IF NOT EXISTS idx_generation_result ON generation_attempts(result_status, failure_type, success_type);

CREATE TABLE IF NOT EXISTS attempt_refs (
    attempt_id TEXT NOT NULL,
    ref_id TEXT NOT NULL,
    duty_role TEXT NOT NULL DEFAULT 'reference', -- action/camera/fx/edit/style/review/post/reference
    usage_mode TEXT NOT NULL DEFAULT 'prompt_only', -- active_input/prompt_only/review_only/offline_grammar
    rank_seen INTEGER,
    rank_chosen INTEGER,
    was_primary INTEGER NOT NULL DEFAULT 0 CHECK(was_primary IN (0,1)),
    was_selected INTEGER NOT NULL DEFAULT 1 CHECK(was_selected IN (0,1)),
    outcome_label TEXT, -- helpful/neutral/harmful/blocked/not_tested
    notes TEXT,
    PRIMARY KEY(attempt_id, ref_id, duty_role),
    FOREIGN KEY(attempt_id) REFERENCES generation_attempts(attempt_id) ON DELETE CASCADE,
    FOREIGN KEY(ref_id) REFERENCES ref_segments(ref_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_attempt_refs_ref ON attempt_refs(ref_id, usage_mode, outcome_label);

-- -----------------------------------------------------------------------------
-- 10. Feedback events and context-aware stats
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS feedback_events (
    feedback_id TEXT PRIMARY KEY,
    attempt_id TEXT,
    retrieval_id TEXT,
    ref_id TEXT NOT NULL,
    context_id TEXT,
    outcome_class TEXT NOT NULL, -- success/partial_success/failure/prompt_only_success/review_only_success/unsafe_blocked/not_tested
    success_scope TEXT, -- action/camera/fx/timing/composition/prompt_transfer/review_guidance
    failure_scope TEXT, -- action/camera/fx/timing/identity/style/attention_conflict/active_input_rejection
    failure_mode TEXT,
    severity INTEGER CHECK(severity BETWEEN 1 AND 5),
    visual_score REAL,
    usefulness_score REAL,
    human_confidence INTEGER CHECK(human_confidence BETWEEN 1 AND 5),
    would_retry_same_context INTEGER CHECK(would_retry_same_context IN (0,1)),
    would_retry_other_context INTEGER CHECK(would_retry_other_context IN (0,1)),
    note TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY(attempt_id) REFERENCES generation_attempts(attempt_id) ON DELETE SET NULL,
    FOREIGN KEY(retrieval_id) REFERENCES retrieval_attempts(retrieval_id) ON DELETE SET NULL,
    FOREIGN KEY(ref_id) REFERENCES ref_segments(ref_id) ON DELETE CASCADE,
    FOREIGN KEY(context_id) REFERENCES scene_contexts(context_id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_feedback_ref_context ON feedback_events(ref_id, context_id, outcome_class);
CREATE INDEX IF NOT EXISTS idx_feedback_attempt ON feedback_events(attempt_id);
CREATE INDEX IF NOT EXISTS idx_feedback_failure ON feedback_events(failure_scope, failure_mode, severity);

CREATE TABLE IF NOT EXISTS ref_context_stats (
    ref_id TEXT NOT NULL,
    key_type TEXT NOT NULL, -- global/coarse/soft/strict/model/task/project
    key_value TEXT NOT NULL,
    used_count INTEGER NOT NULL DEFAULT 0,
    success_count INTEGER NOT NULL DEFAULT 0,
    partial_success_count INTEGER NOT NULL DEFAULT 0,
    failure_count INTEGER NOT NULL DEFAULT 0,
    neutral_count INTEGER NOT NULL DEFAULT 0,
    prompt_only_success_count INTEGER NOT NULL DEFAULT 0,
    review_only_success_count INTEGER NOT NULL DEFAULT 0,
    unsafe_block_count INTEGER NOT NULL DEFAULT 0,
    avg_visual_score REAL NOT NULL DEFAULT 0,
    avg_usefulness_score REAL NOT NULL DEFAULT 0,
    bayes_alpha REAL NOT NULL DEFAULT 1.0,
    bayes_beta REAL NOT NULL DEFAULT 1.0,
    posterior_mean REAL GENERATED ALWAYS AS (
        (success_count + 0.5 * partial_success_count + bayes_alpha) /
        (success_count + partial_success_count + failure_count + neutral_count + bayes_alpha + bayes_beta)
    ) VIRTUAL,
    last_used_at TEXT,
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT,
    PRIMARY KEY(ref_id, key_type, key_value),
    FOREIGN KEY(ref_id) REFERENCES ref_segments(ref_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_ref_context_stats_key ON ref_context_stats(key_type, key_value, posterior_mean);
CREATE INDEX IF NOT EXISTS idx_ref_context_stats_ref ON ref_context_stats(ref_id, used_count, last_used_at);

-- -----------------------------------------------------------------------------
-- 11. Saved searches and GUI/workbench state
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS saved_searches (
    saved_search_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    search_query TEXT,
    mode TEXT,
    filters_json TEXT,
    sort_json TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT
);

CREATE TABLE IF NOT EXISTS workbench_events (
    event_id TEXT PRIMARY KEY,
    event_type TEXT NOT NULL, -- import/search/tag/edit_segment/copy_reference_duty/export/backup
    ref_id TEXT,
    raw_clip_id TEXT,
    payload_json TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    notes TEXT,
    FOREIGN KEY(ref_id) REFERENCES ref_segments(ref_id) ON DELETE SET NULL,
    FOREIGN KEY(raw_clip_id) REFERENCES raw_clips(raw_clip_id) ON DELETE SET NULL
);

-- -----------------------------------------------------------------------------
-- 12. Full-text search: ref_segment search index
-- FTS5 external-content table, synchronized by triggers.
-- -----------------------------------------------------------------------------
CREATE VIRTUAL TABLE IF NOT EXISTS ref_segments_fts USING fts5(
    ref_id UNINDEXED,
    title,
    summary,
    query_text,
    tag_text,
    alias_text,
    risk_text,
    prompt_words_zh,
    prompt_words_en,
    reference_duty,
    do_not_copy,
    review_criteria,
    post_plan,
    edit_timeline_note,
    notes,
    content='ref_segments',
    content_rowid='id',
    tokenize='unicode61 remove_diacritics 1'
);

CREATE TRIGGER IF NOT EXISTS ref_segments_ai AFTER INSERT ON ref_segments BEGIN
  INSERT INTO ref_segments_fts(
    rowid, ref_id, title, summary, query_text, tag_text, alias_text, risk_text,
    prompt_words_zh, prompt_words_en, reference_duty, do_not_copy,
    review_criteria, post_plan, edit_timeline_note, notes
  ) VALUES (
    new.id, new.ref_id, new.title, new.summary, new.query_text, new.tag_text, new.alias_text, new.risk_text,
    new.prompt_words_zh, new.prompt_words_en, new.reference_duty, new.do_not_copy,
    new.review_criteria, new.post_plan, new.edit_timeline_note, new.notes
  );
END;

CREATE TRIGGER IF NOT EXISTS ref_segments_ad AFTER DELETE ON ref_segments BEGIN
  INSERT INTO ref_segments_fts(
    ref_segments_fts, rowid, ref_id, title, summary, query_text, tag_text, alias_text, risk_text,
    prompt_words_zh, prompt_words_en, reference_duty, do_not_copy,
    review_criteria, post_plan, edit_timeline_note, notes
  ) VALUES (
    'delete', old.id, old.ref_id, old.title, old.summary, old.query_text, old.tag_text, old.alias_text, old.risk_text,
    old.prompt_words_zh, old.prompt_words_en, old.reference_duty, old.do_not_copy,
    old.review_criteria, old.post_plan, old.edit_timeline_note, old.notes
  );
END;

CREATE TRIGGER IF NOT EXISTS ref_segments_au AFTER UPDATE ON ref_segments BEGIN
  INSERT INTO ref_segments_fts(
    ref_segments_fts, rowid, ref_id, title, summary, query_text, tag_text, alias_text, risk_text,
    prompt_words_zh, prompt_words_en, reference_duty, do_not_copy,
    review_criteria, post_plan, edit_timeline_note, notes
  ) VALUES (
    'delete', old.id, old.ref_id, old.title, old.summary, old.query_text, old.tag_text, old.alias_text, old.risk_text,
    old.prompt_words_zh, old.prompt_words_en, old.reference_duty, old.do_not_copy,
    old.review_criteria, old.post_plan, old.edit_timeline_note, old.notes
  );
  INSERT INTO ref_segments_fts(
    rowid, ref_id, title, summary, query_text, tag_text, alias_text, risk_text,
    prompt_words_zh, prompt_words_en, reference_duty, do_not_copy,
    review_criteria, post_plan, edit_timeline_note, notes
  ) VALUES (
    new.id, new.ref_id, new.title, new.summary, new.query_text, new.tag_text, new.alias_text, new.risk_text,
    new.prompt_words_zh, new.prompt_words_en, new.reference_duty, new.do_not_copy,
    new.review_criteria, new.post_plan, new.edit_timeline_note, new.notes
  );
END;

-- FTS rebuild command after bulk imports:
-- INSERT INTO ref_segments_fts(ref_segments_fts) VALUES('rebuild');

-- -----------------------------------------------------------------------------
-- 13. Convenience views for GUI/workbench
-- -----------------------------------------------------------------------------
CREATE VIEW IF NOT EXISTS v_ref_search_cards AS
SELECT
    s.ref_id,
    s.title,
    s.primary_ref_type,
    s.source_type,
    s.start_ms,
    s.end_ms,
    s.duration_ms,
    s.thumb_path,
    s.contact_sheet_path,
    s.usage_class,
    s.active_input_allowed,
    s.prompt_influence_allowed,
    s.review_standard_only,
    s.offline_grammar_only,
    s.do_not_use,
    s.review_state,
    s.risk_level,
    s.risk_score,
    s.quality_score,
    s.reuse_score,
    s.success_count,
    s.failure_count,
    s.last_used_at,
    s.reference_duty,
    s.do_not_copy,
    s.prompt_words_zh,
    s.prompt_words_en,
    s.review_criteria,
    s.post_plan,
    COALESCE(GROUP_CONCAT(st.tag_key, ','), '') AS tag_keys
FROM ref_segments s
LEFT JOIN segment_tags st ON s.ref_id = st.ref_id AND st.confirmed = 1
WHERE s.status = 'active'
GROUP BY s.id;

CREATE VIEW IF NOT EXISTS v_active_input_candidates AS
SELECT *
FROM v_ref_search_cards
WHERE active_input_allowed = 1
  AND do_not_use = 0
  AND risk_level IN ('none', 'low');

CREATE VIEW IF NOT EXISTS v_prompt_ready_refs AS
SELECT *
FROM v_ref_search_cards
WHERE review_state IN ('prompt_ready', 'active_safe', 'deep_tagged')
  AND do_not_use = 0;

CREATE VIEW IF NOT EXISTS v_offline_grammar_refs AS
SELECT *
FROM v_ref_search_cards
WHERE offline_grammar_only = 1
  AND active_input_allowed = 0
  AND do_not_use = 0;

CREATE VIEW IF NOT EXISTS v_ref_context_score_summary AS
SELECT
    ref_id,
    key_type,
    key_value,
    used_count,
    success_count,
    partial_success_count,
    failure_count,
    neutral_count,
    prompt_only_success_count,
    review_only_success_count,
    unsafe_block_count,
    avg_visual_score,
    avg_usefulness_score,
    posterior_mean,
    last_used_at
FROM ref_context_stats;

-- -----------------------------------------------------------------------------
-- 14. Common search query examples
-- -----------------------------------------------------------------------------
-- Keyword search with BM25 column weighting. Lower bm25 is better; app may invert/normalize.
-- SELECT s.ref_id, s.title, bm25(ref_segments_fts, 3.5, 1.5, 2.5, 3.2, 2.2, 0.8, 3.0, 3.0, 2.5, 2.5, 1.8, 1.8, 1.5, 0.5) AS bm25_score
-- FROM ref_segments_fts f
-- JOIN ref_segments s ON s.id = f.rowid
-- WHERE ref_segments_fts MATCH 'wet floor skid OR rain splash'
-- ORDER BY bm25_score ASC
-- LIMIT 20;

-- Active-input-safe search should use hard filters, not only risk penalties.
-- SELECT * FROM v_active_input_candidates WHERE tag_keys LIKE '%camera_shake%';
