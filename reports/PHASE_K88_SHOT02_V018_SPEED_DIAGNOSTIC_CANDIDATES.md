# PHASE K88 - SHOT-02-V018 Speed Diagnostic Candidates

## Purpose

V018 was reviewed as a strong positive candidate with a speed note. The human review said the camera, framing, and close-combat relationship are quite good overall, but the rhythm still feels slightly slow.

This phase checks whether local speed-up solves the remaining rhythm issue before spending more Dreamina credits. These are local edit diagnostics only, not new AI generation.

## Source Validation

- Source path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/runs/live/SHOT-02-V018_20260624_235359/SHOT-02-V018_uploadsafe_hard_impact_fast_upperbody.mp4`
- Source exists: true
- Source SHA256: `623877afb9beb6e83d36900507969051884f21239e372d42726c5e52f533b701`
- Source file size bytes: `10147944`
- Source duration seconds: `5.016666666666667`
- Source resolution: `1280x720`
- Source FPS: `24.119601328903656`
- Source frame count: `121`
- Validation tool: `OpenCV cv2.VideoCapture`

## Tools Used

- `ffmpeg`: unavailable in PATH
- `ffprobe`: unavailable in PATH
- Processing tool: Python/OpenCV frame resampling and `mp4v` re-encoding
- Audio preserved: false
- Audio note: No audio preservation was attempted because ffmpeg/ffprobe were unavailable; diagnostic candidates are video-only local edit tests.

## Candidate Outputs

### V018 1.12x

- Output path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/speed_diagnostics/SHOT-02-V018/SHOT-02-V018_speed_1p12x.mp4`
- Exists: true
- SHA256: `d05e106d5731b1b7fc68fb679819f723965edda4dcbd9afb05def3388b92486b`
- File size bytes: `5487849`
- Duration seconds: `4.519071310116086`
- Resolution: `1280x720`
- FPS: `24.12`
- Frame count: `109`
- Validation tool: `OpenCV cv2.VideoCapture`

### V018 1.18x

- Output path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/speed_diagnostics/SHOT-02-V018/SHOT-02-V018_speed_1p18x.mp4`
- Exists: true
- SHA256: `f48ed132f0d8ff9a7c853698e4102900ebedcc86dbfb2f1ad680de96fb044a08`
- File size bytes: `5164289`
- Duration seconds: `4.270315091210613`
- Resolution: `1280x720`
- FPS: `24.12`
- Frame count: `103`
- Validation tool: `OpenCV cv2.VideoCapture`

### V018 1.25x

- Output path: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/edits/speed_diagnostics/SHOT-02-V018/SHOT-02-V018_speed_1p25x.mp4`
- Exists: true
- SHA256: `27c97559badd91344ca5b78dc175aae423a7c1ebc871c8b8aace0eec1bacce59`
- File size bytes: `4934446`
- Duration seconds: `4.021558872305141`
- Resolution: `1280x720`
- FPS: `24.12`
- Frame count: `97`
- Validation tool: `OpenCV cv2.VideoCapture`

## Review Assets

- Review folder: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V018-speed-diagnostics/`
- Comparison contact sheet: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V018-speed-diagnostics/SHOT-02-V018_speed_diagnostics_contact_sheet.jpg`
- 1.12x contact sheet: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V018-speed-diagnostics/SHOT-02-V018_speed_1p12x_contact_sheet.jpg`
- 1.18x contact sheet: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V018-speed-diagnostics/SHOT-02-V018_speed_1p18x_contact_sheet.jpg`
- 1.25x contact sheet: `G:/AICODING/AI_VIDEO/AI_VIDEO_PIPELINE/productions/chi_yan_tian_qiong/reviews/video_reviews/SHOT-02-V018-speed-diagnostics/SHOT-02-V018_speed_1p25x_contact_sheet.jpg`

Generated MP4/JPG files are local review assets only and must not be staged.

## Human Review Guidance

Please compare:

1. Original V018
2. V018 1.12x
3. V018 1.18x
4. V018 1.25x

Evaluation criteria:

- Does rhythm feel better?
- Does hard impact read stronger?
- Does motion become too rushed?
- Do body mechanics remain readable?
- Do identity and camera remain stable?
- Is the best candidate suitable for local edit use?

## Safety Boundaries

- No Dreamina command was run.
- No submit/query/download happened.
- No new AI generation happened.
- Original V018 MP4 was not overwritten.
- No media was staged.
- Upload-safe JPGs were not staged.
- `.vs/` was not staged.
- V013 lock state was not changed.
- V014-R02 shot record was not modified.
- V015 shot record was not modified.
- V016 shot record was not modified.
- V017 shot record was not modified.
- V018 `final_master=false`.
- V018 `locked=false`.

## Final Verdict

SHOT_02_V018_SPEED_DIAGNOSTIC_CANDIDATES_READY_FOR_HUMAN_REVIEW
