# s2aio インストーラ
Scratch 2 オフラインエディタから Auduionoを制御

![s2aio](https://github.com/memakura/s2aio/blob/msi_installer/icons/ScratchArduino.png)
- MrYsLabの s2aio を利用
- Pythonのインストール不要

## インストール
1. FirmataPlus のインストール
    1. https://github.com/MrYsLab/PyMata/tree/master/ArduinoSketch より library.zip をダウンロード
    1. Arduino のライブラリフォルダへ展開 (例: c:\users\<username>\Documents\Arduino)
1. s2aio のインストール
    1. https://github.com/memakura/s2aio/blob/msi_installer/dist/s2aio-1.12-amd64.msi にて [Download] を選ぶ
    1. ダウンロードされた s2aio-1.12-amd64.msi を実行
        1. Windows8以上では「WindowsによってPCが保護されました」と出る場合ので，[詳細情報] をクリックして [実行]
        1. Windows7では「発行元が不明」と出るが[実行]
        1. （このほかウイルスチェックソフトでも発行元が不明に関して何かしら警告が出る可能性あり）
    1. インストール先の例: "C:\Program Files\s2aio" (以下ではここにインストールしたことを仮定)
1. COMポートの設定
    1. Arduino IDE もしくはデバイスマネージャーで Arduino の接続されている COMポート番号 を確認 (以下 COM7 とする)
    1. デスクトップの s2aio のショートカットにて，リンク先を `"C:\Program Files\s2aio\s2aio.exe" COM7` のようにする (Default: COM5)

## 使用方法
1. Arduino 側の設定
    1. Arduino IDEを立ち上げる
    1. IDEの「ファイル」 -> 「スケッチの例」 -> Firmata -> StandardFirmataPlus を読み込み，Arduino へ書き込む
1. Scratch2 側の設定 -> ここスキップできる?
    1. Scratch2 offline editor を立ち上げる
    1. シフトキーを押しながら「ファイル」を押し「実験的なHTTP拡張を読み込み」を選ぶ
    1. "C:\Program Files\s2aio\work\s2aio_ja2.s2e" を選択（このファイルは別の分かりやすい場所にコピーしておいてもよい) (他の言語は ScratchFiles/ExtensionDescriptors)
1. デスクトップ上の s2aio を立ち上げて，最後に「Scratch detected! Ready to rock and roll...」が表示されれば起動完了 -> これも変更

## デバッグ用ログ出力先 -> これも不要?
- C:\Users\(ユーザ名)\AppData\Local\s2aio\log\s2aio_debugging.log

## トラブルシューティング
- ウィンドウがすぐに閉じる場合
    - 他に s2aio が立ち上がっていないか確認
    - 問題が解決しない場合は，ショートカットのリンク先を `cmd /k "C:\Program Files\s2aio\s2aio.exe" COM7` に変更してコンソーに表示されメッセージを読む．
 
 ## ビルド環境
- Python 3.5 (64bit) + cx_Freeze
- Windows 10 (64bit)
