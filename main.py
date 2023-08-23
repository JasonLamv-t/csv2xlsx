import pandas as pd

if __name__ == '__main__':

  print("""
  
 $$$$$$\   $$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\ $$\       $$$$$$\  $$\   $$\ 
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$ |  $$ |$$ |     $$  __$$\ $$ |  $$ |
$$ /  \__|$$ /  \__|$$ |   $$ |\__/  $$ |\$$\ $$  |$$ |     $$ /  \__|\$$\ $$  |
$$ |      \$$$$$$\  \$$\  $$  | $$$$$$  | \$$$$  / $$ |     \$$$$$$\   \$$$$  / 
$$ |       \____$$\  \$$\$$  / $$  ____/  $$  $$<  $$ |      \____$$\  $$  $$<  
$$ |  $$\ $$\   $$ |  \$$$  /  $$ |      $$  /\$$\ $$ |     $$\   $$ |$$  /\$$\ 
\$$$$$$  |\$$$$$$  |   \$  /   $$$$$$$$\ $$ /  $$ |$$$$$$$$\\$$$$$$  |$$ /  $$ |
 \______/  \______/     \_/    \________|\__|  \__|\________|\______/ \__|  \__|
                                                                                
================================================================================
                                                    By JasonLamv-t｜Lin Jiaxiang
                                                       Powder by Python & Pandas
                                  Repo @ https://github.com/JasonLamv-t/csv2xlsx
  """)

  while True:
    csv_file_path = input('请输入要转换的 CSV 文件路径，或将要转换的 CSV 文件拖到此处：').strip('\'"')
    if csv_file_path.endswith('.csv'): break
    else : print('不支持的文件，请重新输入！')

  output_file_path = csv_file_path.removesuffix('.csv').__add__('.xlsx')

  try:
    df = pd.read_csv(csv_file_path)
    df.to_excel(output_file_path, index=False)
  except:
    print('转换失败！')
  else:
    print('转换成功！文件路径：{}'.format(output_file_path))

  exit(0)