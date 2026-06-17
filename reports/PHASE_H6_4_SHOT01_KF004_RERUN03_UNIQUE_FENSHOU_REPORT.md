# SHOT-01-KF-004-rerun-03 Unique Fenshou Constraint Report

## Task
- task_id: SHOT-01-KF-004-rerun-03
- base_task_id: SHOT-01-KF-004
- purpose: add the user-approved unique-Fenshou constraint and run one controlled Dreamina image2image attempt.

## Added prompt sentence
左侧远处那个黑红男性是唯一的焚狩，画面中不允许再出现任何第二个黑红男性轮廓。

## Prompt and safety checks
- prompt path: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\prompts\manual_SHOT-01-KF-004-rerun-03_unique_fenshou_prompt.txt
- manual Branch B direction-fix prompt used as base: yes
- banned center-anchor terms absent: yes
- banned terms checked: 主殿正门, 石阶, 石栏杆, 围绕主殿正门

## Submit
- exact submit command used: C:\Users\msjpurf\bin\dreamina.exe image2image --model_version 4.7 --ratio 16:9 --prompt "图1 作为唯一场景构图与镜头锁定参考。完全保留图1的镜头位置、透视关系和画面构图不变：雨中古寺庭院、湿润石板广场、大面积前景空地、强反光积水、木质主殿、左后方塔楼、彩色经幡、冷灰蓝雨雾氛围全部保留。

图2 作为焚狩角色外观参考，只用于角色外观，不用于站姿构图。保持黑发高束、黑红重甲、男性气质。

图3 作为霜玑角色外观参考，只用于角色外观，不用于站姿构图。保持银蓝高束长发、蓝白银轻甲长衣、女性气质。

生成一张半写实3D武侠电影关键帧。

画面中只有两个人：一个焚狩，一个霜玑。没有第三人，没有重复角色，没有分身。

最重要的空间关系如下：

焚狩位于画面左侧远处区域，落点在左侧回廊与左后方建筑前的湿石板地带，只能看到较小的黑红男性轮廓。焚狩必须明显远离镜头，属于远景小人物，严格遵循近大远小。焚狩在画面中的存在感要被主动压低，属于远景对峙目标，而不是近景展示主体。不要把焚狩拉近，不要让焚狩进入中景主体区，不要让焚狩变成清晰大人物。

霜玑位于画面右侧远处区域，落点在主殿右前方广场的右侧内侧区域，只能看到较小的银蓝女性轮廓。霜玑也必须明显远离镜头，人物尺寸与焚狩接近，可略大一点点，但仍然严格属于远景层。霜玑在画面中的存在感同样要被主动压低，属于远景对峙目标，而不是近景展示主体。不要把霜玑拉近，不要让霜玑进入中景主体区，不要让霜玑变成清晰大人物。

霜玑必须明确朝向左侧的焚狩。霜玑身体向画面左侧转身，呈明显侧身或轻微侧背姿态，面部朝向画面左侧，视线明确投向左侧远处的焚狩。霜玑不是正面站立，不是面朝镜头，不是看向观众，不是角色展示海报姿态。霜玑只能看到侧脸或四分之三侧脸，不要出现正面脸朝向镜头的效果。

这是双远景同层对峙。两人必须分别占据画面左右两侧的远处区域，不能靠在一起，不能同时落在同一侧区域。两人之间必须隔着明显的大面积空旷湿石板地，中间留出清楚的对峙空间。焚狩在左，霜玑在右，二人横向距离要明显拉开。不要把两人收拢到主殿前同一片区域，不要让两人站得过近。

特别强调人物朝向：焚狩与霜玑彼此对峙，双方都应把注意力投向对方，而不是面向镜头。霜玑必须朝左看向焚狩，不能正面看镜头，不能朝向画外，不能像独立角色立绘。

重点是：两人都远，两人都小，但左右明确分开；焚狩是左侧远景小轮廓，霜玑是右侧远景小轮廓；二人之间有明显的大面积空广场；镜头和背景构图不变。

保留冷灰蓝低饱和雨天光线、湿石板反光、细密雨丝、电影感、肃杀安静氛围。

不要文字，不要水印，不要设定卡，不要三视图，不要四联图，不要多余人物，不要第二个焚狩，不要第二个霜玑，不要把焚狩拉近，不要把霜玑拉近，不要让任何角色贴边，不要让任何角色正面看镜头。
左侧远处那个黑红男性是唯一的焚狩，画面中不允许再出现任何第二个黑红男性轮廓。" --images G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-SC-TEMPLE-COURTYARD-001_locked_ancient_temple_rain_courtyard.png --images G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-CH-A-SUBJECT-001_locked_fenshou_full_body_subject.png --images G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\locked_refs\A-CH-B-SUBJECT-001_locked_shuangji_full_body_subject.png --resolution_type 2k
- run_dir: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260615_230829_SHOT-01-KF-004-rerun-03
- submit_id: 263433e5-e46a-411b-a0f5-ad7497c556a8

## Query
- exactly one query_result was run: yes
- query_status: querying
- download_happened: False
- output_path: not downloaded
- integrity: not available

## Artifacts
- provider_requests: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260615_230829_SHOT-01-KF-004-rerun-03\provider_requests.jsonl
- provider_responses: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260615_230829_SHOT-01-KF-004-rerun-03\provider_responses.jsonl
- job_store: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260615_230829_SHOT-01-KF-004-rerun-03\job_store.json
- execution_log: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\runs\live\20260615_230829_SHOT-01-KF-004-rerun-03\execution_log.txt
- prompt_json: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\prompts\shot_01_keyframe_prompt_SHOT-01-KF-004-rerun-03.json
- manifest_csv: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\manifests\production_image2image_SHOT-01-KF-004-rerun-03.csv
- shot_record: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\shots\shot_01_keyframe_record_SHOT-01-KF-004-rerun-03.json
- review_note: G:\AICODING\AI_VIDEO\AI_VIDEO_PIPELINE\productions\chi_yan_tian_qiong\reviews\image_reviews\SHOT-01-KF-004-rerun-03_unique_fenshou_review.md

## Safety proof
- no retry happened: yes
- no batch happened: yes
- no parallel task happened: yes
- runtime code modified: no
- configs/providers.json modified: no
- source files modified: no
- writes remained inside workspace: yes

## Final verdict
SHOT01_KF004_RERUN03_SUBMITTED_QUERYING
