import pandas as pd

def main():
    df = pd.read_csv('database/ingredient/mext.csv', index_col=1)
    df = df.replace({'Tr': '0', '-': '0', '†': '', '\(': '', '\)': '', '\*': '0'}, regex=True)
    df = df.astype(float)
    df = df.fillna(0)
    df_main = df[['l_class','WATER', 'PROT-', 'FAT-', 'CHOCDF-', 'FIB-', 'NACL_EQ', 
                    'NA', 'K', 'CA', 'MG', 'P', 'FE', 'ZN', 'CU', 'MN', 
                    'VITD', 'VITK ', 'THIA', 'RIBF', 'VITB6A', 'VITB12', 'VITC']]
    df_main['VITE'] = df['TOCPHA'] + df['TOCPHB'] + df['TOCPHG'] + df['TOCPHD']

    df_db = df_main[(df['l_class'] != 18) & (df['l_class'] != 15)]
    df_db = df_main[(df['l_class'] != 18) & (df['l_class'] != 15)]
    df_db['ingredient'] = df_db.apply(food_or_seasoning, axis=1)
    df_db.to_csv('database\ingredient.csv', encoding='utf-8')

def food_or_seasoning(x):
    if x['l_class'] == 16 or x['l_class'] == 17:
        return 'seasoning'
    else:
        return 'food'

if __name__ == "__main__":
    main()