# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import DWIExtract


def test_DWIExtract_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bval_scale=dict(argstr='-bvalue_scaling %s',
    ),
    bzero=dict(argstr='-bzero',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    grad_file=dict(argstr='-grad %s',
    ),
    grad_fsl=dict(argstr='-fslgrad %s %s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_bval=dict(),
    in_bvec=dict(argstr='-fslgrad %s %s',
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    nobzero=dict(argstr='-nobzero',
    ),
    nthreads=dict(argstr='-nthreads %d',
    nohash=True,
    ),
    out_file=dict(argstr='%s',
    mandatory=True,
    position=-1,
    ),
    shell=dict(argstr='-shell %s',
    sep=',',
    ),
    singleshell=dict(argstr='-singleshell',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = DWIExtract.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DWIExtract_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = DWIExtract.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
