## Setup:

- To create the environment, use 
```
conda env create -f environment.yml
```

- #To activate this environment `tfenv`, use
```
conda activate tfenv
```

- To deactivate an active environment, use
```
conda deactivate
```

- To export `tfenv` environment, use
```
conda env export -n tfenv > environment.yml
```

- To update `tfenv` environment, use
```
conda env update -f environment.yml --prune 
```