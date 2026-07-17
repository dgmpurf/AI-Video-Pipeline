# CAL-001 Human Manifest Review Checklist

This checklist records human review only. P1-R2 does not pre-fill acceptance.

- [ ] Exactly 84 manifest rows.
- [ ] Exactly 7 families.
- [ ] Exactly 4 prompt architectures per family.
- [ ] Exactly 3 replicates per architecture.
- [ ] Exactly 28 prompt files.
- [ ] Exactly 84 package files.
- [ ] No missing or extra matrix cell.
- [ ] Fixture paths, hashes, metadata, and rights status are acceptable.
- [ ] Every active generation input is eligible for this internal calibration.
- [ ] Prompt targets have project-wide calibration value.
- [ ] No airborne-flyout benchmark is included.
- [ ] No external copyrighted active input is included.
- [ ] No wall/body collision test is included.
- [ ] Budget arithmetic is correct.
- [ ] Expected result counts are one video and zero images per row.
- [ ] Every package and manifest row remains no-submit with all authority flags false.
- [ ] Stop conditions remain binding.
- [ ] Official Source is unchanged.
- [ ] CAL-001B is excluded.
- [ ] final_master=false for every row.
- [ ] locked=false for every row.

human_manifest_reviewed=true
human_manifest_accepted=true
reviewer=human_user
review_date=2026-07-18
accepted_repository_commit=2bf8dd0292066f41b956193d399a0a0cf9d2f47e
acceptance_text_sha256=617be14a783179c64266ef9afa0ce5b8d0c44d24b16dc389c4c58ed1c91ac738
accepted_manifest_sha256=b2ecfb87899feca784fc8e1f2b751fc181aeab9a9118a3a7609067d4b92b2c6d
accepted_fixture_registry_sha256=cf35a7ea15e4c51e4d6936f9a796f90215445f059503cd29bd6eccb8c7658142
accepted_prompt_inventory_sha256=27c95725e80c325693894f8b04cc3587f404f971559fbf1c2cc9292b3a361d6d
accepted_package_inventory_sha256=b716cb063977172a8fcf28359c4ceef00b9ad0f90524a3ee675d194fb79c251c
accepted_full_experiment_inventory_sha256=448a2d473b06bf4b5f8548644733fdd68af7cb37749bc8d807bf69e53ef96138
P2_nonblocking_notes_accepted=true
execution_authority_active=false
next_phase=CAL-001-P3_ACTIVATION_PRECONDITION_AUDIT
notes=Acceptance is bound to the recorded commit, canonical acceptance-text hash, and five immutable artifact digests. This review does not activate execution authority.
