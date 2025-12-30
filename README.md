# ROS2用CPU使用率モニタコマンドパッケージ

## 概要
- 本パッケージはCPU使用率を取得してROS2のトピックとして配信するノードと、その情報を読み込み表示するノードから構成されるROS2パッケージです。

## 機能概要
- システムのCPU使用率を一定周期で取得します。
- 取得したCPU使用率はROS2のトピック通信を用いて配信されます。
- PublisherノードがCPU使用率を取得し、数値データとしてPublishします。
- Subscriberノードがトピックを読み込み、受信したCPU使用率を標準出力に表示します。

## 使用方法

### 実行方法

#### メイン端末でPublisherノードを起動
```
ros2 run robosysros2_pkg cpu_usage_publisher
```
#### 別端末でSubscriberノードを起動
```
ros2 run robosysros2_pkg cpu_usage_listener
```
### 実行例

#### Subscriber
```
[INFO] [cpu_usage_listener]: Listen: CPU Usage: 12.5%
```
### エラー例

#### 必要なライブラリがインストールされていない場合
```
ModuleNotFoundError: No module named 'psutil'
```
- psutilをインストールしてください

## テスト

### このプログラムでは、以下のテストを実施しています。
```
GitHub Actions上での自動ビルド
cpu_usage_listener単体起動時の動作確認
cpu_usage_publisher単体起動時の動作確認
ublisher/Listenerを同時起動した際のトピック通信確認
Ctrl+Cによるノード終了時の例外処理の確認
timeoutコマンドによる自動終了時の挙動確認
```

### テスト環境
```
OS: Ubuntu 22.04
ROS 2: Humble Hawksbill
Python: 3.10
```

## 必要なソフトウェア
```
ROS 2 Humble Hawksbill
Python 3.10
psutil (CPU 使用率取得のため)
```

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布及び使用が許可されます。
- © 2025 Rintatrou Matunaga
