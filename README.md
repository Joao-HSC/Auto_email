I think this .exe can only work if your operating system is Windows x64.
You can execute this .exe everyday after the market closes (or not), if you wish to receive an e-mail with the ticker symbol of a stock that belongs to the VQFY ETF if they had a price change of over 7% or under -7%.
You can change the .csv with the constituents of another ETF or any other list of stocks.
If you wish to automate this process, set up a task schedule in your Windows options and in the auto_email.py change the e-mail from the input to your actual e-mail in between ''. Also, remove the prints.
Please don't forget to change your e-mail in the auto_email.py file and rebuild the file.
