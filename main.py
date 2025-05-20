print(f"{'Placa Solar'} | {'Assistente'} | {'Disp. Goodwe'} | {'Eficiência (%)'} | {'Ef <70%'}  | {'Saída'}")
print("-" * 75)  

# Tabela verdade com verificação de eficiência usando 
for placaSolar in range(2):
    for assistente in range(2):
        for eficiencia_percent in [65, 80]:  # Simulando eficiências: abaixo e acima de 70%

            # Define se a eficiência está abaixo de 70%
            ef_abaixo_70 = 1 if eficiencia_percent < 70 else 0

            for disp_goodwe in range(2):

                # Regra lógica: SE eficiência está abaixo de 70% E todos os outros são True
                out = 1 if ( ef_abaixo_70 and (placaSolar and assistente and disp_goodwe)) else 0

                # Cores (ANSI) 
                cor_entrada = "\033[94m"  # Azul
                cor_saida = "\033[92m" if out == 1 else "\033[91m"  # Verde ou Vermelho
                reset_cor = "\033[0m"

                print(
                    f"{cor_entrada}{placaSolar:^11}{reset_cor} | "
                    f"{cor_entrada}{assistente:^10}{reset_cor} | "
                    f"{cor_entrada}{disp_goodwe:^14}{reset_cor} | "
                    f"{cor_entrada}{eficiencia_percent:^14}{reset_cor} | "
                    f"{cor_entrada}{ef_abaixo_70:^9}{reset_cor} | "
                    f"{cor_saida}{out:^5}{reset_cor}"
                )