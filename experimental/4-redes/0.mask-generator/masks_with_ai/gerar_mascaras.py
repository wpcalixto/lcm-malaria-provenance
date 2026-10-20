#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Masks from stored segmentation coordinates
# File type:
#     Script
# Purpose:
#     Generates masks from segmentation coordinates stored in a CSV file (exploratory step).
# Repository:
#     lcm-malaria-provenance, component experimental
# Version:
#     v1.0.0
# Date:
#     2026-10-20
# Developer:
#     Prof. Wesley Pacheco Calixto
# Authors:
#     Sthefanie Monica Premebida, Federal University of Technology - Parana, Brazil, ORCID 0000-0002-8964-2119
#     Gabrielly Queiroz Pereira, State University of Ponta Grossa, Brazil, ORCID 0000-0003-2663-0783
#     Philipp Wiedemann, Department of Biotechnology, Mannheim University of Applied Sciences, Germany
#     Marcella Scoczynski R. Martins, Federal University of Technology - Parana, Brazil, ORCID 0000-0002-5716-4968
#     Wesley Pacheco Calixto, Institute of Systems and Robotics, University of Coimbra, Portugal, ORCID 0000-0002-1928-4432
# Corresponding author:
#     Wesley Pacheco Calixto, wesley.pacheco@isr.uc.pt, Institute of Systems and Robotics, University of Coimbra
# License:
#     MIT
# Citation:
#     If you use this code, please cite:
#     Premebida, S. M., Pereira, G. Q., Wiedemann, P., Martins, M. S. R., & Calixto, W. P. (2026). Low-Cost Microscope dataset, code, and model checkpoints for Computational provenance in external evaluation of deep learning for malaria microscopy (Version 1.0.0) [Data set and software]. Zenodo. https://doi.org/10.5281/zenodo.23505452
# Related publication:
#     Computational provenance in external evaluation of deep learning for malaria microscopy (DOI not yet available).
# Inputs:
#     - resultados_segmentacao_v2.csv
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - cv2
#     - numpy
#     - pandas
# Execution:
#     python 4-redes/0.mask-generator/masks_with_ai/gerar_mascaras.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     The input CSV (resultados_segmentacao_v2.csv) belongs to an exploratory folder that is not included in this record.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
import pandas as pd
import numpy as np
import cv2
import os
import re
import ast

def parse_coordenadas(coord_str):
    """
    Função para extrair uma ou mais listas de polígonos da string de coordenadas.
    Usa expressões regulares para encontrar todos os polígonos.
    """
    # A expressão regular encontra todos os padrões "poligono_xy": [[...]]
    # e captura apenas o conteúdo dentro dos colchetes externos.
    matches = re.findall(r'"poligono_xy":\s*(\[\[.*?\]\])', coord_str)
    
    poligonos = []
    for match in matches:
        try:
            # ast.literal_eval é uma forma segura de converter uma string de lista/dicionário Python
            # para o objeto Python correspondente.
            poligono = ast.literal_eval(match)
            poligonos.append(poligono)
        except (ValueError, SyntaxError):
            # Ignora polígonos malformados se houver algum
            print(f"Aviso: Não foi possível processar o polígono: {match}")
            continue
            
    return poligonos

# --- CONFIGURAÇÃO ---
# Altere estes caminhos conforme a sua estrutura de arquivos
CSV_PATH = 'resultados_segmentacao_v2.csv' # Caminho para o seu arquivo CSV
OUTPUT_MASKS_DIR = 'mascaras_geradas'      # Pasta onde as máscaras serão salvas

# --- LÓGICA PRINCIPAL ---

# 1. Criar o diretório de saída se ele não existir
if not os.path.exists(OUTPUT_MASKS_DIR):
    os.makedirs(OUTPUT_MASKS_DIR)
    print(f"Diretório '{OUTPUT_MASKS_DIR}' criado.")

# 2. Carregar o CSV com o pandas
try:
    df = pd.read_csv(CSV_PATH)
    print(f"CSV '{CSV_PATH}' carregado com sucesso. Total de {len(df)} linhas.")
except FileNotFoundError:
    print(f"Erro: O arquivo CSV '{CSV_PATH}' não foi encontrado. Verifique o caminho.")
    exit()

# 3. Iterar sobre cada linha do DataFrame para processar cada imagem
for index, row in df.iterrows():
    caminho_imagem = row['caminho_da_imagem']
    nome_imagem = row['nome_da_imagem']
    coordenadas_str = row['coordenadas_poligonos']
    
    # Verifica se o caminho da imagem original existe
    if not os.path.exists(caminho_imagem):
        print(f"Aviso: Imagem não encontrada em '{caminho_imagem}'. Pulando linha {index + 2}.")
        continue

    try:
        # 4. Ler a imagem original para obter suas dimensões (altura e largura)
        img_original = cv2.imread(caminho_imagem)
        if img_original is None:
            print(f"Aviso: Falha ao ler a imagem '{caminho_imagem}'. Pulando.")
            continue
            
        altura, largura, _ = img_original.shape

        # 5. Criar uma máscara preta (array de zeros) com as mesmas dimensões da imagem original
        # A máscara será de canal único (escala de cinza)
        mascara = np.zeros((altura, largura), dtype=np.uint8)

        # 6. Extrair os polígonos da string
        poligonos = parse_coordenadas(coordenadas_str)

        if not poligonos:
            print(f"Aviso: Nenhum polígono válido encontrado para a imagem '{nome_imagem}'. Máscara ficará preta.")
        else:
            # Converte os pontos dos polígonos para o formato que o OpenCV espera
            # (uma lista de arrays NumPy de inteiros de 32 bits)
            poligonos_np = [np.array(p, dtype=np.int32) for p in poligonos]
            
            # 7. Desenhar os polígonos preenchidos na máscara
            # A cor 255 representa o branco, que é o padrão para máscaras binárias
            cv2.fillPoly(mascara, poligonos_np, color=255)

        # 8. Salvar a máscara gerada
        # É uma boa prática salvar máscaras em formato sem perdas, como .png
        nome_mascara = os.path.splitext(nome_imagem)[0] + '.png'
        caminho_saida = os.path.join(OUTPUT_MASKS_DIR, nome_mascara)
        cv2.imwrite(caminho_saida, mascara)
        
        print(f"Máscara para '{nome_imagem}' salva em '{caminho_saida}'.")

    except Exception as e:
        print(f"Ocorreu um erro ao processar a imagem '{nome_imagem}': {e}")

print("\nProcesso concluído!")