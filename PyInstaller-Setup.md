When to Use binaries vs datas

### binaries:

Use this for compiled files (e.g., .dll, .so, .pyd) or entire directories that need to be included as-is.
Example:

```
binaries=[("C:\\path\\to\\compiled_file.dll", "destination_folder")]
```

### datas:

Use this for non-compiled files (e.g., .txt, .json, .png) or specific files from a directory.
Example:

```
datas=[("C:\\path\\to\\file.txt", "destination_folder")]
```
