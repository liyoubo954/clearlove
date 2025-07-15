(function () {
  const response = {
    "type": "page",
    // 配置页面标题（可选，根据需求决定是否显示）
    "body": {
      "type": "container",
      // Flex 布局让内容水平+垂直居中
      "style": {
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        // 让容器占满视口高度，确保内容垂直居中
        "minHeight": "calc(100vh - 120px)", 
        "textAlign": "center"
      },
      "body": {
        "type": "text",
        "value": "欢迎您登录系统",
        // 标题级别，1 最大，可按需调整
        "level": 1, 
        "style": {
          "fontSize": "36px",  // 字体大小
          "color": "#2f54eb", // 字体颜色，选个好看的蓝色
          "fontWeight": "bold", // 加粗
          "textShadow": "2px 2px 4px rgba(0, 0, 0, 0.1)" // 文字阴影，更精致
        }
      }
    }
  };
  window.jsonpCallback && window.jsonpCallback(response);
})();