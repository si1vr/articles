---
uuid: 53be5097-f0ea-938b-0794-3c6e865cb573
title: redirect
comments: false
toc: false
count: false
date: 2024-12-15 13:56:44
layout:
share_menu:
donate:
license:
qrcode:
---


<script>
window.onload = function() {
  // 获取URL中的goto参数
  const params = new URLSearchParams(window.location.search);
  const goto = params.get('goto');
  
  if (goto) {
    // 可以在这里添加提示或确认框
    
    window.location.href = goto;
  } else {
    window.location.href = '/'; // 如果没有goto参数则返回首页
  }
}
</script>

<p style="text-align: center">正在重定向到外部链接，请稍候...</p>