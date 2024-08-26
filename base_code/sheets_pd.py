import pandas as pd

def create_data_frame(scraper_dict):
    def check_lengths(data):
        lengths = [len(v) for v in data.values()]
        if len(set(lengths)) > 1:
            print("As colunas têm comprimentos diferentes!")
            for key, value in data.items():
                print(f"{key}: {len(value)}")
        else:
            print("Todos os arrays têm o mesmo comprimento.")

    check_lengths(scraper_dict)
    
    dts = pd.DataFrame(scraper_dict)
    dts.to_excel('busca_precos.xlsx', index=False)