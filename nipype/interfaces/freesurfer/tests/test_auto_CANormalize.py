# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import CANormalize


def test_CANormalize_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        atlas=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-3,
        ),
        control_points=dict(
            argstr="-c %s",
            extensions=None,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-4,
        ),
        long_file=dict(
            argstr="-long %s",
            extensions=None,
        ),
        mask=dict(
            argstr="-mask %s",
            extensions=None,
        ),
        out_file=dict(
            argstr="%s",
            extensions=None,
            hash_files=False,
            keep_extension=True,
            name_source=["in_file"],
            name_template="%s_norm",
            position=-1,
        ),
        subjects_dir=dict(),
        transform=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-2,
        ),
    )
    inputs = CANormalize.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CANormalize_outputs():
    output_map = dict(
        control_points=dict(
            extensions=None,
        ),
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = CANormalize.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
