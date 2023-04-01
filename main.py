import random
from util.chart import create_chart_from_csv
from config import CHUNK_SIZE, INIT_MINT, TX_AMOUNT
from util.mint import mintBst
from util.redeem import redeemBnusd
from util.getters import getBstSupply, getBnUsdInContract, getBstPrice, one_percent_chance, five_percent_chance, getRedeemAmount


# a main function that simulates the whole process
#  first part is just creating a csv file with the simulation data
def simulate(test_run):
    file_name = f'simulation_local_{test_run}.csv'
    
    # to set start of range
    cache_num = 0 
    
    # check if file exists, if so ask prompt if user wants to append
    try:
        with open(file_name, 'r') as f:
            # prompt user if they want to append
            print('File exists, do you want to append?')
            print('type yes or no')
            choice = input('Enter choice: ')
            if choice == 'yes':
                # get the last tx number
                last_line = f.readlines()[-1]
                last_tx = last_line.split(',')[0]
                last_tx = int(last_tx)
                
                # set start of range to last tx + 1
                cache_num = last_tx + 1

                # add new line to file
                with open(file_name, 'a') as f:
                    f.write('\n')
                pass
            else:
                print('Exiting program')
                exit()

    except Exception as e:
        print(e)
        print('File does not exist, creating file')
        
        # create csv file with headers
        with open(file_name, 'w') as f:
            f.write('tx, mint_w_bnusd, redeem_bst_amount,bnusd_in_contract,bst_supply,bst_price\n')

    # initial mint
    init_mint = INIT_MINT
    mintBst(init_mint)

    init_bst_price = getBstPrice()
    init_bnusd_in_contract = getBnUsdInContract()
    init_bst_supply = getBstSupply()

    # add genesis tx to csv file
    with open(file_name, 'a') as f:
        f.write(f'init,{init_mint},0,{init_bnusd_in_contract},{init_bst_supply},{init_bst_price}\n')

    # start loop
    for i in range(cache_num, TX_AMOUNT):
        mint_amount = 0
        redeem_amount = 0

        # expecting a few large mints in the beginning
        if i < 5:
            # mint
            mint_amount = random.randint(3000,5000)
            mintBst(mint_amount)
        
        else:
            #  50/50 chance for mint or redeem
            mint_or_redeem = random.randint(0,1)
              
            if mint_or_redeem == 0:
                # mint
                
                # one percent chance of large mint
                if one_percent_chance():
                    mint_amount = random.randint(2000,5000)
                # five percent chance of medium mint
                elif five_percent_chance():
                    mint_amount = random.randint(400,4000)
                # every 50th tx is a large mint
                elif i % 50 == 0:
                    mint_amount = random.randint(4000,8000)
                # 94 percent chance of small mint
                else:
                    mint_amount = random.randint(10,300)

                mintBst(mint_amount)

            else:
                # redeem              
                redeem_amount = getRedeemAmount()
                redeemBnusd(redeem_amount)

        amount_of_bnusd_in_contract = getBnUsdInContract()
        bst_supply = getBstSupply()
        bst_price = getBstPrice()

        # add tx to csv file
        with open(file_name, 'a') as f:
            f.write(f'{i},{mint_amount},{redeem_amount},{amount_of_bnusd_in_contract},{bst_supply},{bst_price}\n')

    # print progress
    create_chart_from_csv(file_name, CHUNK_SIZE, init_mint )

simulate(1)