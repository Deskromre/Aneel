import pandas as pd

#codigo para transformar da base semanal para a diaria - ELMER

#leitura do arquivo
df = pd.read_csv('CVU_F.csv', sep =';')

# Conversão de coluna para o datetime para ficar mais fácil
df['dat_iniciosemana'] = pd.to_datetime(df['dat_iniciosemana'], format='%Y-%m-%d')
df['dat_fimsemana'] = pd.to_datetime(df['dat_fimsemana'], format='%Y-%m-%d')

# criando um novo dataframe pra receber os dados diarios
CVU_DIARIO_2024_df = pd.DataFrame()

#loop que vai preencher os dados diarios no dateframe que criei

for index, row in df.iterrows():
    diferença_dias = row['dat_fimsemana'] - row['dat_iniciosemana']
    numero_dias = diferença_dias.days + 1 #o +1 é pra considerar a última data também
    intervalo_datas = pd.date_range(start=row['dat_iniciosemana'], end=row['dat_fimsemana'])

    for date in intervalo_datas:
        valor_cvu_diario = round(row['val_cvu'] / numero_dias, 3)
    valor_diario_df = pd.DataFrame({
        'dia': intervalo_datas,
        'ano_referencia': row['ano_referencia'],
        'mes_referencia': row['mes_referencia'],
        'num_revisao': row['num_revisao'],
        'nom_semanaoperativa': row['nom_semanaoperativa'],
        'cod_modelos': row['cod_modelos'],
        'id_subsistema': row['id_subsistema'],
        'nom_subsistema': row['nom_subsistema'],
        'nom_usina': row['nom_usina'],
        'val_cvu': valor_cvu_diario
    })
    CVU_DIARIO_2024_df = pd.concat([CVU_DIARIO_2024_df, valor_diario_df], ignore_index=True)

# Arrumando as colunas 
CVU_DIARIO_2024_df = CVU_DIARIO_2024_df[['dia', 'ano_referencia', 'mes_referencia', 'num_revisao', 'nom_semanaoperativa', 
                           'cod_modelos', 'id_subsistema', 'nom_subsistema', 'nom_usina', 'val_cvu']]

# Checar se está tudo nos conformes
print(CVU_DIARIO_2024_df.head())

# Salvar a nova tabela transformada
CVU_DIARIO_2024_df.to_csv('CVU_2024_DIARIO.csv', index=False)
