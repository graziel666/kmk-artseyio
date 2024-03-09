import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP2,  # column
    source=board.GP0, # row
    # boot_device=1,
    # cdc=True,
    # midi=True,
    # mouse=True,
    storage=True,
    # keyboard=True,
    usb_id=('The Programming Raccoon', 'Quagboard-Ardux'),
)
