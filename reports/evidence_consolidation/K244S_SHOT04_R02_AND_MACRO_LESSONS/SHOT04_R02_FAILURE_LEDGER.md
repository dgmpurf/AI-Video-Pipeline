# SHOT-04 R02 Failure Ledger

## Scope

This ledger consolidates failure evidence from K201 through K244 for SHOT-04 R02. It is written for ChatGPT Pro Extended Source synthesis and is evidence-only, not official Source.

## Chronological Failure Narrative

K201-K212 built a Source-governed wall-impact route around the rainy temple wall-panel reference. The package chain remained no-submit until human authorization, and K212 found the fixed package ready to request L3 submit authorization.

K213 was the first authorized live submit for the four-reference `multimodal2video` package. It returned a `submit_id`, but `gen_status=fail` during resource upload. K214 triaged this as an upload-phase problem, not a visual-generation failure. The local reference existed and was readable; the likely causes were upload host timeout, large PNGs, and path/packaging fragility. The decision was upload-safe package-local reference packaging rather than retrying.

K217/K218/K219 proved that the upload-safe video route could produce and download a local MP4. K220B then failed that candidate visually: the intended shoulder/forearm drive, received force, body-wall causality, rebound timing, and action density did not read. This was not a Source absence or local package parse failure; it was a model execution failure in the generated video.

K225/K226 shifted to a four-reference `image2image` micro-impact keyframe. The package reviewed successfully and the submit was accepted, but the one authorized query returned `gen_status=fail` with no image result and no download URL.

K229/K230 simplified that keyframe route to three references. The same valid-submit remote final-generation failure repeated, which downgraded reference count as the sole explanation.

K234/K235 removed image references entirely and tried a softened prompt-only `text2image` wall-contact probe. That also failed remotely after a valid submit.

K240/K241 removed exact body-wall contact and wall damage from the positive target, using an alternate near-wall guard-clash prompt-only `text2image` probe. That still failed remotely after a valid submit. K241F therefore broadened the diagnosis from exact wall-contact brittleness to dual-character close-combat / guard-contact staging brittleness in still/keyframe routes.

K242V-K244 moved back toward video because the earlier video route at least produced media. K244 passed the prompt-only `text2video` package review with high-risk notes, leaving K245 as the next human authorization decision, not an already-run phase.

## Failure Table

| Phase | Route | Result | Failure Type | Immediate Decision |
| --- | --- | --- | --- | --- |
| K213/K214 | 4-ref `multimodal2video` wall-impact submit | `submit_id` returned but `gen_status=fail`; no queued generation | upload resource failure | Create upload-safe package-local refs; no retry |
| K219/K220B | upload-safe `multimodal2video` wall-impact video | media downloaded, but action failed visually | visual/model execution failure | Stop direct 5s full-action route; keyframe-first route |
| K225/K226 | 4-ref `image2image` micro-impact keyframe | accepted submit, one query returned `gen_status=fail` | remote final-generation failure | simplify to 3-ref package |
| K229/K230 | 3-ref `image2image` micro-impact keyframe | accepted submit, one query returned `gen_status=fail` | repeated remote final-generation failure | route reset; compare softened/text-only/manual routes |
| K234/K235 | softened prompt-only `text2image` wall-contact probe | accepted submit, one query returned `gen_status=fail` | triple remote generation failure | human route decision; consider alternate action |
| K240/K241 | prompt-only `text2image` near-wall guard-clash probe | accepted submit, one query returned `gen_status=fail` | fourth valid-submit remote failure | plan video route; still/keyframe routes blocked for now |

## What Failed

- Uploading large/complex references failed in K213 before a valid queued generation.
- Full-length video generation produced media in K219 but did not realize the intended wall-impact action in K220B.
- Exact body-wall contact keyframe generation failed remotely in both 4-ref and 3-ref `image2image` routes.
- Softened wall-contact `text2image` failed remotely despite no active refs.
- Alternate near-wall guard-clash `text2image` also failed remotely despite removing body-wall contact and wall damage.

## What Did Not Fail

- `sources/` governance was preserved throughout the inspected phases.
- Package JSON and manifest parsing passed in reviewed packages.
- Human authorization boundaries were generally preserved: one submit, one query, one download where authorized.
- Login/auth was not the cause when preflight, submit, and query succeeded.
- Query/download misuse was not the cause in the valid-submit failures; failed tasks had no result media or download URL.
- The K217/K218/K219 video route proved that this account/project environment can receive downloadable video media.
- K220A review artifact creation succeeded after the video download.
- K243V/K244 package creation and review succeeded for the next text2video route, but that route has not been submitted.

## Causes Excluded

The following causes are excluded or downgraded by the evidence:

- Source governance was not the cause.
- Local package parsing was not the cause for valid-submit failures.
- Missing local reference files were not the cause for K213; K214 found the failed architecture reference existed locally.
- Auth/login was not the cause when preflight and submit succeeded.
- Query/download misuse was not the cause.
- Reference count alone was not the cause after the 3-ref route failed.
- Exact wall-contact alone was not the cause after the near-wall guard-clash route failed without body-wall contact.

## Causes Upgraded

The following causes were upgraded:

- Upload-safe path/asset preparation matters for live submits using local media references.
- Full 5s video prompts can technically succeed while failing the intended micro-action.
- Dual-character close-contact, guard compression, and body-wall or near-wall staging are provider/model brittle.
- Prompt-only `text2image` is not automatically safer than video for this combat staging class.
- Repeated valid-submit remote final-generation failure is stronger evidence than a single visual failure.
- Video route can return media but may fail visually/action-wise.

## Route Decisions Caused by Failures

- K214 moved from original refs to upload-safe package-local refs.
- K221 moved from direct 5s wall-impact video to micro-impact keyframe-first planning.
- K226F moved from 4-ref image2image to 3-ref image2image.
- K230F reset away from reference stripping toward softened/contact alternatives.
- K235F stopped exact or softened wall-contact keyframe generation pending human strategy decision.
- K237A/K238 moved to alternate near-wall guard-clash, removing body-wall contact and wall damage.
- K241F/K242V moved away from still/keyframe generation toward prompt-only text2video because video had at least produced media before.
- K244 left K245 as one-submit-only after human authorization, not as an automatic continuation.

## Current Unresolved Risks

- K245 text2video may produce a remote failure, or it may produce media that still fails visually.
- Prompt-only video has identity continuity risk because there are no active refs.
- Dual-character combat can still collapse into hand-push, static pose-out, extra limbs, duplicated bodies, or weak force transfer.
- A 5s legal duration may still contain only a 1.0s-1.5s useful edit window.
- Source update candidates require separate ChatGPT/human governance and must not be applied directly by Codex.

## Important Conclusions

- Source governance was not the cause.
- Local package parsing was not the cause for valid-submit failures.
- Auth/login was not the cause when preflight and submit succeeded.
- Query/download misuse was not the cause.
- Exact wall-contact was a candidate cause, but the later guard-clash `text2image` failure broadened diagnosis to dual-character close-combat staging brittleness.
- Video route can return media but may fail visually/action-wise.
