import subprocess

if __name__ == "__main__":
    notebooks_to_run = ['predictor/2_edge2vec_embedding.ipynb', 'predictor/3_predictor.ipynb']

    for i in range(10):
        print(f'Time {i}')
        for notebook in notebooks_to_run:
            cmd = f'jupyter nbconvert --execute --inplace {notebook}'
            subprocess.run(cmd, shell=True)