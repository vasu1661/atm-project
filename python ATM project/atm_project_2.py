import pandas as pd
from datetime import datetime


while True:
    print('1-Balance enquiry')
    print('2-Deposit')
    print('3-Withdraw')
    print('4-Exit')
    choice = int(input('\nplease choice your type of transactions:'))
    if choice == 4:
        break
    df = pd.read_csv('new_file.csv')
    input_card_num = int(input("Enter card number:"))
    index = df.index[df['card_number'] == input_card_num].tolist()[0]
    # index = df.index[df['card_number'] == input_card_num].tolist()
    # print(index,index)

    status = df.loc[df['card_number'] == input_card_num, 'status']
    # index1 = df.reset_index[df['card_number'] == input_card_num,'status' ]
    # print(index1)

    if status.empty:
        print("Card is not Valid")
    else:
        # print(status[0])
        if status[index] == 'Active':
            dc = pd.read_csv('cust_trans.csv')
            new_trans_id = dc.get('trans_ID').max() + 1
            print(new_trans_id)
            today = datetime.today()
            transaction_dict = {'trans_ID': [new_trans_id], 'trans_date': [today],'tran_type': [''], 'trans_amt': [''], 'card_number': [input_card_num], 'trans_status': ['']}

            if choice == 1:
                transaction_dict['tran_type'] = 'Balance Enquiry'
                transaction_dict['trans_amt'] = 0
                max_tries = 3

                while max_tries > 0:
                    input_pin_num = int(input("Enter pin number:"))
                    pin_number = df.loc[df['card_number'] == input_card_num, 'PIN'][index]
                    if input_pin_num == pin_number:

                        bal_output = df.loc[df['PIN'] == pin_number, 'balance']
                        print("Balance is : ", bal_output[index])
                        transaction_dict['trans_status'] = 'Success'
                        break
                    else:
                        print("PIN not valid")
                        max_tries = max_tries - 1

                if transaction_dict['trans_status'] == '':
                    transaction_dict['trans_status'] = 'Failure'
                    df.at[index, 'status'] = 'Blocked'
                    df.to_csv('new_file.csv', index=False, sep=',')

            if choice == 2:
                deposit_amount = int(input("Enter amount to deposit:"))
                transaction_dict['tran_type'] = 'Deposit'
                transaction_dict['trans_amt'] = deposit_amount
                max_tries = 3
                while max_tries > 0:
                    input_pin_num = int(input("Enter pin number:"))
                    pin_number = df.loc[df['card_number'] == input_card_num, 'PIN'][index]
                    if input_pin_num == pin_number:
                        bal_output = df.loc[df['PIN'] == pin_number, 'balance']
                        new_balance = bal_output[index] + deposit_amount
                        df.at[index, 'balance'] = new_balance
                        print("Amount deposited.")
                        print("New Balance is : ", new_balance)
                        df.to_csv('new_file.csv', index=False, sep=',')
                        transaction_dict['trans_status'] = 'Success'
                        break
                    else:
                        print("PIN not valid" 'you have left with', max_tries)
                        max_tries = max_tries - 1

                if transaction_dict['trans_status'] == '':
                    transaction_dict['trans_status'] = 'Failure'
                    df.at[index, 'status'] = 'Blocked'
                    df.to_csv('new_file.csv', index=False, sep=',')

            if choice == 3:
                withdraw_amount = int(input("Enter amount to withdraw:"))
                transaction_dict['tran_type'] = 'Withdrawal'
                transaction_dict['trans_amt'] = withdraw_amount
                max_tries = 3
                while max_tries > 0:
                    input_pin_num = int(input("Enter pin number:"))
                    pin_number = df.loc[df['card_number'] == input_card_num, 'PIN'][index]
                    if input_pin_num == pin_number:
                        bal_output = df.loc[df['PIN'] == pin_number, 'balance']

                        if withdraw_amount > bal_output[index]:
                            transaction_dict['trans_status'] = 'Failure'
                        else:
                            new_balance = bal_output[index] - withdraw_amount
                            df.at[index, 'balance'] = new_balance
                            print("Amount is withdrawn")
                            print("New Balance is : ", new_balance)
                            print(df)
                            df.to_csv('new_file.csv', index=False, sep=',')
                            transaction_dict['tran_type'] = 'Withdrawal'
                            transaction_dict['trans_amt'] = withdraw_amount

                            transaction_dict['trans_status'] = 'Success'
                        break
                    else:
                        print("PIN not valid")
                        max_tries = max_tries - 1

                if transaction_dict['trans_status'] == ['']:
                    transaction_dict['trans_status'] = 'Failure'
                    df.at[index, 'status'] = 'Blocked'
                    df.to_csv('new_file.csv', index=False, sep=',')
                    print('trans successful')

            print(transaction_dict)
            up = pd.DataFrame(transaction_dict)
            update_trans = up.to_csv('cust_trans.csv', mode='a', index=False, header=False)
            print(update_trans)
        else:
            print("Card is not Active")
