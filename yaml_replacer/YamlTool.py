import sys
import os

def replace(filter_file_path, replace_file_path):
  parent_dir = os.path.dirname(os.getcwd())
  with open(filter_file_path, "r") as fin:
    with open(replace_file_path, "r") as frep:
      filters = fin.read().splitlines()
      replaces = frep.read().splitlines()
      filter_lines = len(filters)
      replace_lines = len(replaces)
      if filter_lines != replace_lines:
        print("Filter and Replace files do not have the same number of lines")
        return
      # print(filters)
      # print(replaces)
      for filter, replace in zip(filters, replaces):
        for root, dir, files in os.walk(parent_dir):
          if(root == os.path.join(parent_dir, "yaml_replacer")):
            continue
          for file in files:
            with open(os.path.join(root, file), "r") as f:
              file_data = f.read()
            file_data = file_data.replace(filter, replace)
            with open(os.path.join(root, file), "w") as f:
              f.write(file_data)


if __name__ == '__main__':
  command_args = sys.argv[1]
  file_path_1 = sys.argv[2]
  file_path_2 = sys.argv[3]

  if command_args == "replace":
    replace(file_path_1, file_path_2)
