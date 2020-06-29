import os

# rename readme
os.rename("README.zh_CN.md", "README.md")

search_path = '.' 
root, dirs, files = next(os.walk(search_path), ([],[],[]))

dirs = [directory for directory in dirs if not directory.startswith(".")]
countFiles = 0
                
for directory in dirs:
    rootdir = directory
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            fileRaw = os.path.join(subdir, file)
            fileName = os.path.basename(fileRaw)
            fileNameOrigin = os.path.splitext(fileName)[0].replace(".zh_CN", "")
            os.rename(fileRaw, f"{subdir}/{fileNameOrigin}.md")
            countFiles += 1
            
print(f"Number of replaced files: {countFiles}")