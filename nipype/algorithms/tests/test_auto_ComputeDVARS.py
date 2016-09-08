# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ...testing import assert_equal
from ..confounds import ComputeDVARS


def test_ComputeDVARS_inputs():
    input_map = dict(figdpi=dict(usedefault=True,
    ),
    figformat=dict(usedefault=True,
    ),
    figsize=dict(usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(mandatory=True,
    ),
    in_mask=dict(mandatory=True,
    ),
    save_all=dict(usedefault=True,
    ),
    save_nstd=dict(usedefault=True,
    ),
    save_plot=dict(usedefault=True,
    ),
    save_std=dict(usedefault=True,
    ),
    save_vxstd=dict(usedefault=True,
    ),
    series_tr=dict(),
    )
    inputs = ComputeDVARS.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_ComputeDVARS_outputs():
    output_map = dict(avg_nstd=dict(),
    avg_std=dict(),
    avg_vxstd=dict(),
    fig_nstd=dict(),
    fig_std=dict(),
    fig_vxstd=dict(),
    out_all=dict(),
    out_nstd=dict(),
    out_std=dict(),
    out_vxstd=dict(),
    )
    outputs = ComputeDVARS.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
