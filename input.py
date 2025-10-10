
def prompt_int(str):
    while True:
        try:
            return(int(input(str)))
        except ValueError:
            print("数値を入力してください。")
        except KeyboardInterrupt:
            return(False)
        except Exception:
            return(False)

if __name__=="__main__":
    a = prompt_int("なにか数字を入力：")
    if a == False:
        print ("キャンセルですね。")
    else:
        print(f"入力値= {a}")
