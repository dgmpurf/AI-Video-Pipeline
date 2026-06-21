# SHOT-02-V010 Single Submit and Review Prep

## 1) Canary

- executable: C:/Users/msjpurf/bin/dreamina.exe
- ersion result: {"version":"46b5b0e-dirty","commit":"46b5b0e","build_time":"2026-06-03T19:39:25Z"}
- user_credit result: {"total_credit":2667,"user_id":1611200923726843,"vip_level":"maestro"}
- canary status: PASS

## 2) Command-contract preflight

- dreamina image2video -h checked; --image supported and required.
- atio is inferred from input image; command should omit ratio (confirmed).
- seedance2.0_vip duration range includes 4 (4–15), resolution supports 720p.
- preflight status: PASS

## 3) Submit

- exact submit command:

`powershell
C:/Users/msjpurf/bin/dreamina.exe image2video --image "productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V009/SHOT-02-V009_frame_1p00s.jpg" --prompt-file "productions/chi_yan_tian_qiong/prompts/manual_SHOT-02-V010_followup_forearm_clash_sidestep_counter_prompt.txt" --model_version seedance2.0_vip --duration 4 --video_resolution 720p --poll 0
`

- submit response summary:
  - submit_id: 6967b1fb-cd5d-42ba-b461-29d861ef1738
  - logid: 2026062121331416925404700887980F2
  - credit_count: 56
  - gen_status: querying
- prompt file verified UTF-8 readable and present
- input image verified present

## 4) Query/download follow-up

- ran once: dreamina query_result --submit_id 6967b1fb-cd5d-42ba-b461-29d861ef1738 --download_dir productions/chi_yan_tian_qiong/runs/live/SHOT-02-V010_20260621_213314
- query response summary:
  - gen_status: querying
  - queue_status: Queueing
  - queue_idx: 1
  - queue_length: 1
  - priority: 1
- no download yet (still queued/querying)

## 5) Shot record update

- updated: productions/chi_yan_tian_qiong/shots/shot_02_video_record_SHOT-02-V010.json
- status: submitted_querying
- package_status: submitted_querying
- human_review_status: pending
- final_master: alse
- locked: alse

## 6) Notes

- no retry
- no resubmit
- no lock
- final approval still requires human review
