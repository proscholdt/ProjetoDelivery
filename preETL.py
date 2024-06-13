import pandas as pd

# Carregar o arquivo CSV
file_path = '/content/drive/MyDrive/orders.csv'
df = pd.read_csv(file_path)

# Função para converter hora AM/PM para 24 horas
def convert_to_24h(time_str):
    # Verificar se a string de tempo é AM ou PM
    if 'PM' in time_str:
        # Se for PM, adicionar 12 horas
        time_obj = pd.to_datetime(time_str, format='%m/%d/%Y %I:%M:%S %p')
        return time_obj.strftime('%Y-%m-%d %H:%M:%S')
    elif 'AM' in time_str:
        # Se for AM, não adicionar horas
        time_obj = pd.to_datetime(time_str, format='%m/%d/%Y %I:%M:%S %p')
        return time_obj.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return time_str  # Caso contrário, retornar como está

# Aplicar a função de conversão às colunas relevantes
time_columns = [
    'order_moment_created',
    'order_moment_accepted',
    'order_moment_ready',
    'order_moment_collected',
    'order_moment_in_expedition',
    'order_moment_delivering',
    'order_moment_delivered',
    'order_moment_finished'
]

for col in time_columns:
    if col in df.columns:
        df[col] = df[col].apply(lambda x: convert_to_24h(x) if pd.notnull(x) else x)

# Salvar o dataframe atualizado em um novo arquivo CSV
output_path = '/content/orders.csv'
df.to_csv(output_path, index=False)
