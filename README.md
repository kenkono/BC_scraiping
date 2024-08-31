# BC_scraiping
## 動作手順
### Docker デスクトップのインストール
https://www.docker.com/ja-jp/products/docker-desktop/
### コマンドで以下を実施
```
Dockerイメージのビルド:
docker build -t biccamera_scraiping .

Dockerコンテナの実行:
Windows の PowerShellの場合
docker run --rm -v ${PWD}:/app biccamera_scraiping
Macの場合
docker run --rm -v $(pwd):/app biccamera_scraiping

```