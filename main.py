import tkinter as tk
import logging
from pprint import pprint

from connectors.binance_futures import BinanceFuturesClient

#### Logger
logger = logging.getLogger()

logger.setLevel(logging.INFO)

# Stream Handler
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

# File Handler
file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# logger.debug("This message is important only when debugging the programm")
# logger.info("This message just shows basic information")
# logger.warning("This message is about something you should pay attention to")
# logger.error("This message helps to debug an error that occurred in your program")



### initialize and start program
if __name__ == '__main__':

    binance = BinanceFuturesClient("8e21c90e564c21b508d9e85fcd19052e9e98befb7c6d6c6c63a4171f0d6a16eb",
                                   "e70d44562302b27a16a1fce5d5b7cf420fe4735c5959353409f5226af9979069", True)
    






    
    # pprint(binance.get_balances(), sort_dicts=False)
    # order = binance.place_order("BTCUSDT", "BUY", 0.01, "LIMIT", price=20000, tif="GTC")
    # pprint(order, sort_dicts=False)
    # pprint(binance.get_order_status("BTCUSDT", order['orderId']), sort_dicts=False)
    # pprint(binance.cancel_order("BTCUSDT", order['orderId']), sort_dicts=False)



    # create window
    #root = tk.Tk()
    # keep window and wait for actions
    #root.mainloop()


    # root.configure(bg='gray12')

    # # grid parameter
    # i = 0
    # j = 0

    # # fonts
    # calibri_font = ("Calibri", 11, "normal")

    # # show contracts
    # for contract in bitmex_contracts:
    #     label_widget = tk.Label(root, text=contract, bg='gray12', fg='SteelBlue1', width=13, font=calibri_font)
    #     label_widget.grid(row=i, column=j, sticky='ew')

    #     if i == 4:
    #         j += 1
    #         i = 0
    #     else:
    #         i += 1

    

