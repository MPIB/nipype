# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..io import FreeSurferSource


def test_FreeSurferSource_inputs():
    input_map = dict(
        hemi=dict(
            usedefault=True,
        ),
        subject_id=dict(
            mandatory=True,
        ),
        subjects_dir=dict(
            mandatory=True,
        ),
    )
    inputs = FreeSurferSource.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_FreeSurferSource_outputs():
    output_map = dict(
        BA_stats=dict(
            altkey="BA",
            loc="stats",
        ),
        T1=dict(
            extensions=None,
            loc="mri",
        ),
        annot=dict(
            altkey="*annot",
            loc="label",
        ),
        aparc_a2009s_stats=dict(
            altkey="aparc.a2009s",
            loc="stats",
        ),
        aparc_aseg=dict(
            altkey="aparc*aseg",
            loc="mri",
        ),
        aparc_stats=dict(
            altkey="aparc",
            loc="stats",
        ),
        area_pial=dict(
            altkey="area.pial",
            loc="surf",
        ),
        aseg=dict(
            extensions=None,
            loc="mri",
        ),
        aseg_stats=dict(
            altkey="aseg",
            loc="stats",
        ),
        avg_curv=dict(
            loc="surf",
        ),
        brain=dict(
            extensions=None,
            loc="mri",
        ),
        brainmask=dict(
            extensions=None,
            loc="mri",
        ),
        curv=dict(
            loc="surf",
        ),
        curv_pial=dict(
            altkey="curv.pial",
            loc="surf",
        ),
        curv_stats=dict(
            altkey="curv",
            loc="stats",
        ),
        entorhinal_exvivo_stats=dict(
            altkey="entorhinal_exvivo",
            loc="stats",
        ),
        filled=dict(
            extensions=None,
            loc="mri",
        ),
        graymid=dict(
            altkey=["graymid", "midthickness"],
            loc="surf",
        ),
        inflated=dict(
            loc="surf",
        ),
        jacobian_white=dict(
            loc="surf",
        ),
        label=dict(
            altkey="*label",
            loc="label",
        ),
        norm=dict(
            extensions=None,
            loc="mri",
        ),
        nu=dict(
            extensions=None,
            loc="mri",
        ),
        orig=dict(
            extensions=None,
            loc="mri",
        ),
        pial=dict(
            loc="surf",
        ),
        rawavg=dict(
            extensions=None,
            loc="mri",
        ),
        ribbon=dict(
            altkey="*ribbon",
            loc="mri",
        ),
        smoothwm=dict(
            loc="surf",
        ),
        sphere=dict(
            loc="surf",
        ),
        sphere_reg=dict(
            altkey="sphere.reg",
            loc="surf",
        ),
        sulc=dict(
            loc="surf",
        ),
        thickness=dict(
            loc="surf",
        ),
        volume=dict(
            loc="surf",
        ),
        white=dict(
            loc="surf",
        ),
        wm=dict(
            extensions=None,
            loc="mri",
        ),
        wmparc=dict(
            extensions=None,
            loc="mri",
        ),
        wmparc_stats=dict(
            altkey="wmparc",
            loc="stats",
        ),
    )
    outputs = FreeSurferSource.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
