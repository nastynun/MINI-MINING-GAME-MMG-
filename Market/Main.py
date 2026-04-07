
import time
import math
import random
from Beautiful import *
from pprint import pprint
from threading import Thread


decor = "=" * 40
decor2 = "*" * 40
decor3 = "_" * 40

Miner_Market = {
    'Free-Miner':     {'BUY': 0,     'SELL': 10,    'HTZ': 10,    'SEC': 3.5, 'chance': 0},
    'Mini-Miner':     {'BUY': 200,   'SELL': 100,   'HTZ': 50,    'SEC': 3,   'chance': 35},
    'Medium-miner':   {'BUY': 400,   'SELL': 200,   'HTZ': 70,    'SEC': 2.5, 'chance': 25},
    'Common-miner':   {'BUY': 600,   'SELL': 300,   'HTZ': 160,   'SEC': 2,   'chance': 18},
    'Rare-miner':     {'BUY': 1000,  'SELL': 500,   'HTZ': 200,   'SEC': 1.5, 'chance': 10},
    'Epic-miner':     {'BUY': 1500,  'SELL': 700,   'HTZ': 500,   'SEC': 1,   'chance': 6},
    'Legendary-miner':{'BUY': 2000,  'SELL': 1000,  'HTZ': 1000,  'SEC': 1,   'chance': 3.5},
    'Mytic-miner':    {'BUY': 5000,  'SELL': 2500,  'HTZ': 1500,  'SEC': 1,   'chance': 1.5},
    'Trans-miner':    {'BUY': 15000, 'SELL': 5000,  'HTZ': 5000,  'SEC': 1,   'chance': 0.9},
    'LastGod-miner':  {'BUY': 50000, 'SELL': 25000, 'HTZ': 13000, 'SEC': 1,   'chance': 0.1},
}

profit_Bost = {
    'Free':         {'BUY': 0,      'SELL': 10,    'BST': 0.05, 'chance': 0},
    'Common-Boost': {'BUY': 1000,   'SELL': 500,   'BST': 0.15, 'chance': 45},
    'Rare-Boost':   {'BUY': 1500,   'SELL': 700,   'BST': 0.20, 'chance': 30},
    'Epic-Boost':   {'BUY': 15000,  'SELL': 3000,  'BST': 0.25, 'chance': 15},
    'Legd-Boost':   {'BUY': 20000,  'SELL': 5000,  'BST': 0.30, 'chance': 7},
    'mytic-Boost':  {'BUY': 30000,  'SELL': 15000, 'BST': 0.40, 'chance': 2.5},
    'GOD-Boost':    {'BUY': 100000, 'SELL': 45000, 'BST': 0.47, 'chance': 0.5},
}

class Miner_Holder:
    def __init__(self,Name,alias):
        self.Name = Name
        self.Balance = 0
        self.Miner = 'Free Miner'
        self.Boost = 0.05
        self.BoostName = 'Free'
        self.Speed = 3.5
        self.HTZ = 5
        self.Mining = False
        self.Mined = 0
        self.alias = alias
        self.Tax  = self.Balance - (self.Balance - 0.15 * self.Balance)
        self.Invenotry= {'MINERS':{},
                        'BOOSTS':{}}
        

    def Roll_Miner(self):

        if not self.Balance >= 3000:
            red_bg(f"You don't Suffient Balance To Carry Our This Task Please Retry! ❌")
            return


        Total_Weight = sum(e.get('chance',0) for e in Miner_Market.values())
        Rolled = random.uniform(0,Total_Weight)
        
        current = 0

        for Miner_Name, stats in Miner_Market.items():
            current += stats.get('chance',0)
            if Rolled <= current:
                self.Balance -= 3000

                green(f'You Have Succefuly Rolled {Miner_Name}!')
                self.Add_item(Miner_Name,'MINERS','Miner_Market')
                current = 0
                return Miner_Name
        return None

    def Roll_Boost(self):

        if not self.Balance >= 3000:
            red_bg(f"You don't Suffient Balance To Carry Our This Task Please Retry! ❌")
            return


        Total_Weight = sum(e.get('chance',0) for e in profit_Bost.values())
        Rolled = random.uniform(0,Total_Weight)

        current = 0

        for Boost_Name, stats in profit_Bost.items():
            current += stats.get('chance',0)
            if Rolled <= current:
                self.Balance -= 3000
                green(f"You Have Succefuly Rolled {Boost_Name}! ✅")
                self.Add_item(Boost_Name,'BOOSTS','profit_Bost')
                current = 0
                return Boost_Name

        return None

    def Add_item(self,item,catigory,market):
        
        try:

            if market == 'profit_Bost':

                self.Invenotry[catigory][item] = profit_Bost[item]
                
            elif market == 'Miner_Market':
                self.Invenotry[catigory][item] = Miner_Market[item]
            print('_')
            style(f"You Have Succeful Added {item} to your Invenotry ✅ ",bold=True,color=81)

        except:
            style(text=f"UNKNOWN ERRO Please Retry! ❌",
            bold=True,
            underline=True,
            color=225,
            bg=9)
    
    def ShowInventory(self):
        for Name , item in self.Invenotry.items():
            style(Name, color=120, bold=True)
            style(item,bold=True,color=207)

    def Use_Miner(self,Name):
        for Miners,stats in self.Invenotry['MINERS'].items():
            print("_"*40)
            if Miners == Name:
                self.Miner = Miners
                self.HTZ = stats.get('HTZ',0)
                self.Speed = stats.get('SEC',0)
                style(F"You are now using {Name}",bold=True, color=123,underline=False)
            else:
                style(F"You Do not own this item!",bold=True, color=196,underline=True)
            
            print("_"*40)

    def Use_Boost(self,Name):
        for Avabst,stats in self.Invenotry['BOOSTS'].items():
            print("_"*40)

            if Avabst == Name:
                self.Boost = stats.get('BST',0)
                self.BoostName = Avabst
                self.Speed = stats.get('HTZ',0)

                style(F"You are now using {Name}",bold=True, color=123,underline=False)

            else:
                style(F"You Do not own this item!",bold=True, color=196,underline=True)
            
            print("_"*40)

    def __str__(self):
        line = "═" * 35

        style(f"👋 Hey {self.Name} ({self.alias})", bold=True, color=200)
        print(f"\n{line}")
        style("📊 CURRENT STATS", bold=True, color=45)
        print(f"{line}\n")

        print(f"{'Name:':<22} {self.Name}")
        print(f"{'Alias:':<22} {self.alias}")
        print(f"{'Balance:':<22} ${self.Balance:,.2f}")

        print("\n" + "─" * 35 + "\n")

        print(f"{'Miner:':<22} {self.Miner}")
        print(f"{'Currently:':<22} {self.Mining}")
        print(f"{'Booster:':<22} {self.Boost*100:.0f}%")
        print(f"{'Boost Model:':<22} {self.BoostName}")
        print(f"{'Mining Rate:':<22} ${self.HTZ:,.0f}")
        print(f"{'Mining Speed:':<22} {self.Speed}")
        print(f"{'Tax Paid:':<22} ${self.Tax:,.2f}")

        print(f"\n{line}")
        style("⚡ Available Stats", bold=True, color=118)
        return line
        
    def Mine(self):
        
        if self.Mining == True:
            self.Mining = False
            style("Your Miners Have Stopped Mining!", bold=True, color=203)
            strt = Thread(target=self.Start_Mining)
            strt.start()

        else:
            self.Mining = True
            style("Your Miners Have Started Mining!", bold=True, color=82)
            strt = Thread(target=self.Start_Mining)
            strt.start()
    
    def Start_Mining(self):

        if self.Mining == True:
            style("Miners Are NOW Started Mining!", bold=True, color=40)
        
        while self.Mining:
            self.Mined += self.HTZ
            time.sleep(self.Speed)
    
    def calculate_tax(self, amount):
        """Calculates a progressive tax based on the amount being claimed."""
        if amount < 1000:
            rate = 0.05  # 5% tax for small amounts
        elif amount < 10000:
            rate = 0.10  # 10% tax
        else:
            rate = 0.15  # 15% tax for high earners
        
        tax_total = amount * rate
        return tax_total

    def Claim(self):
        # Calculate raw earnings
        raw_amt = (self.Mined * self.Boost) + self.Mined
        
        if raw_amt < 1:
            style(f"Nothing to collect yet!", color=166, bold=True)
            return

        # Calculate Tax
        tax_amount = self.calculate_tax(raw_amt)
        final_amt = raw_amt - tax_amount
        
        # Update Player Stats
        self.Balance += final_amt
        self.Tax += tax_amount # Tracking lifetime tax paid
        
        print("-" * 30)
        style(f"💰 Gross Earnings: ${raw_amt:,.2f}", color=40)
        style(f"💸 Tax Deducted ({int((tax_amount/raw_amt)*100)}%): -${tax_amount:,.2f}", color=196)
        style(f"✅ Net Profit: ${final_amt:,.2f}", color=46, bold=True)
        print("-" * 30)
        
        self.Mined = 0 # Reset mining buffer
    
    def BuyItem(self,Item_Name,market):
        Avaible = None
        try:
           Avaible = market[Item_Name]
        except:
            style(f"Invalid items! ❌",color=198,bold=True,underline=True)
            return
            
        for Stuff, values in market.items():
    
            if Stuff == Item_Name:
                if market == profit_Bost:
                    Price = values.get('BUY')
                    if self.Balance >= Price:
                        self.Balance -= Price
                        self.Add_item(Item_Name,'BOOSTS','profit_Bost')
                        print('_'*40)
                        style(f"You Succefuly Bought {Item_Name}",color=48,bold=True)
                        print('_'*40)
                        break
                    else:
                        style(f"You Have Insufficent Balance! ❌",
                                                        color=198,
                                                        bold=True,underline=True)
                        break
                        
                elif market == Miner_Market:
                    Price = values.get('BUY')
                    if self.Balance >= Price:
                            self.Balance -= Price
                            self.Add_item(Item_Name,'MINERS','Miner_Market')
                            print('_'*40)
                            style(f"You Suffeculy Bought {Item_Name}",color=48,bold=True)
                            print('_'*40)
                            break
                    else:
                        style(f"You Have Insufficent Balance! ❌",
                                                            color=198,
                                                            bold=True,underline=True)
                        break
    
    def sell_item(self,item):

        try:
            done = False
            for item_name, stats in self.Invenotry.items():
                for key, val in stats.items():
                    if key == item:
                        self.Invenotry[item_name].pop(key)
                        sell = val.get("SELL",0)
                        self.Balance += sell
                        style(f"Succefuly Deleted {item_name}!",bold=True,color=224,bg=82)
                        done = True

            if not done:
                style(f"Can't Delete Unknown Item {item}!",bold=True,color=255,bg=160)

        except:
            style(f"Can't Delete Unknown Item {item}!",bold=True,color=255,bg=160)
            return
    

def ShowMarket():
    pprint(profit_Bost)
    print("="*40)
    pprint(Miner_Market)



def Main():
    print("\033[92m" + "="*40 + "\n   MINI MINING GAME (MMG)\n" + "="*40 + "\033[0m")
    user_name = input("Enter Name: ")
    user_alias = input("Enter Alias: ")
    player = Miner_Holder(user_name, user_alias)

    while True:
        print("\n" + "_"*40)
        print(f"💰 Balance: ${player.Balance:,.2f} | ⛏️ Mined: ${player.Mined:,.2f} | ⚙️ Miner: {player.Miner}")
        print("Commands: [1] Stats [2] Market [3] Roll Miner [4] Roll Boost [5] Mine/Stop [6] Claim [7] Inventory [8] Use [9] Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            print(player)
        elif choice == '2':
            ShowMarket()
        elif choice == '3':
            player.Roll_Miner()
        elif choice == '4':
            player.Roll_Boost()
        elif choice == '5':
            player.Mine()
        elif choice == '6':
            player.Claim()
        elif choice == '7':
            player.ShowInventory()
        elif choice == '8':
            cat = input("Use (miner/boost)?: ").lower()
            item = input("Enter item name exactly: ")
            if "miner" in cat: player.Use_Miner(item)
            else: player.Use_Boost(item)
        elif choice == '9':
            style("Thanks for playing!", color=200)
            player.Mining = False
            break
        else:
            style("Invalid Choice!", color=196)

if __name__ == "__main__":
    Main()