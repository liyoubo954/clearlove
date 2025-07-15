(function () {
  // 添加项目名称映射表
  const projectNameMap = {
    'tongsujiayong': '通苏嘉甬', 
    'shanghaijichanglianluoxian': '上海机场联络线', 
    'suzhous1': '苏州S1', 
    'qinwangtongdao': '秦望通道', 
    'shenjiangtielu': '深江铁路', 
    'shanshantielu': '汕汕铁路', 
    'jingbintielu': '京滨铁路', 
    'jingtangtielu': '京唐铁路', 
    'xiangyalu': '湘雅路', 
    'beijings6': '北京S6', 
    'jianningxilu': '建宁西路', 
    'shanghainanhuizhixian': '上海南汇支线',
    'guangaogang': '广澳港',
    'huanggangluchuanhuangsuidao': '黄岗路穿黄隧道',
    'beijings6': '北京S6',
    'changjiutielu': '昌九铁路',
    'qingdaoersui': '青岛二隧',
    'wuhanditie12haoxian': '武汉地铁12号线',
    'haizhuwansuidao': '海珠湾隧道',
    'guangshengang': '广深港',
    'shanghainanhuizhixian': '上海南汇支线',
    'meixi': '美溪',
    'shenzhen5': '深圳5',
    'nanjingsihao': '南京四号线',
    'nanfengtielu': '南丰铁路',
    'chongqingwanshuntielu': '重庆涪陵铁路',
    'tianjingangxian': '津港高铁',
    'nanjingguojimihu': '南京国际秘湖',
    'wuhanxinganxian': '武汉新港线',
    'wuhan11': '武汉11',
    'buquanshiliao': '补充资料(原系统)',
    'wuhu':'芜湖',
    'nanjing11': '南京11',
    'qingdaoersuidadungou': '青岛二隧大盾构',
    'jiangmingertongdao': '江明二通道',
    'ninghuangbeiyan': '宁黄北延',
    'guangzhantielu': '广湛铁路',
    'dongliuhuan': '东六环',
    'jiangxinzhou': '江心洲',
    'suzhou6-9': '苏州6-9',
    'ziliaomuban': '资料模板',
    'tongpanlu': '桐泮路',
    'lianshanlu': '良山路',
    'xiasalu': '下沙路',
    'hepingdadao': '和平大道',
    'wuhannanhusuidao': '武汉南湖隧道',
    'qingdao': '青岛（土建）',
    'chuandianxiangmu': '川滇项目',
    'xiamenfuhaoxian': '厦门6号线',
    'nanjing7haoxian': '南京7号线'
};
  const response = {
    "type": "page",
    "body": [
      {
        "type": "crud",
        "syncLocation": false,
        "loadDataOnce": false,
        "pageSize": 10,
        "filter": {
          "title": "项目搜索",
          "body": [
            {
              "type": "input-text",
              "name": "project_name",
              "label": "项目名称",
              "placeholder": "请输入项目名称（支持中文或英文）",
              "clearable": true
            }
          ]
        },
        "api": {
          "url": "/remote_file/list_projects",
          "method": "get",
          "data": {
            "project_name": "${project_name}"
          },
          "adaptor": `
            return {
              status: 0,
              data: {
                items: payload.map(project => ({
                  project: project,
                  projectName: (${JSON.stringify(projectNameMap)})[project.toLowerCase()] || project,
                  id: project
                }))
              }
            };
          `
        },
        "columns": [
          {
            "name": "project",
            "label": "项目名称",
            "type": "button",
            "label": "${projectName}",
            "html": true,
            "level": "link",
            "actionType": "dialog",
            "dialog": {
              "title": "${projectName} - 文件列表",
              "size": "lg",
              "body": {
                  "type": "service",
                  "data": {
                    "currentProject": "${project}"
                  },
                  "api": {
                    "url": "/remote_file/list_project_files",
                    "method": "get",
                    "data": {
                      "project_name": "${project}",
                      "sub_path": ""
                    },
                    "adaptor": `
                       const projectName = api.query.project_name || api.data.project_name;
                       return {
                         status: 0,
                         data: {
                           items: payload.map(item => ({
                             label: item.name,
                             value: '/data_sdd2/minio/minio_data/' + projectName + '/' + item.name,
                             type: item.is_dir ? 'folder' : 'file',
                             size: item.is_dir ? '-' : (item.size / 1024).toFixed(1) + ' KB',
                             last_modified: new Date(Number(item.last_modified) * 1000).toLocaleString(),
                             currentProject: projectName
                           }))
                         }
                       };
                     `
                  },
                "body": [
                  {
                    "type": "table",
                    "name": "fileTable",
                    "source": "${items}",
                    "columns": [
                      {
                         "name": "label",
                         "label": "文件名",
                         "type": "container",
                         "body": [
                           {
                             "type": "tpl",
                             "tpl": "<i class='fa ${type === 'folder' ? 'fa-folder' : (label.toLowerCase().endsWith('.pdf') ? 'fa-file-pdf-o' : label.toLowerCase().endsWith('.doc') || label.toLowerCase().endsWith('.docx') ? 'fa-file-word-o' : label.toLowerCase().endsWith('.xls') || label.toLowerCase().endsWith('.xlsx') ? 'fa-file-excel-o' : label.toLowerCase().endsWith('.ppt') || label.toLowerCase().endsWith('.pptx') ? 'fa-file-powerpoint-o' : label.toLowerCase().endsWith('.jpg') || label.toLowerCase().endsWith('.jpeg') || label.toLowerCase().endsWith('.png') || label.toLowerCase().endsWith('.gif') ? 'fa-file-image-o' : label.toLowerCase().endsWith('.zip') || label.toLowerCase().endsWith('.rar') || label.toLowerCase().endsWith('.7z') ? 'fa-file-archive-o' : label.toLowerCase().endsWith('.mp4') || label.toLowerCase().endsWith('.avi') || label.toLowerCase().endsWith('.mov') ? 'fa-file-video-o' : label.toLowerCase().endsWith('.mp3') || label.toLowerCase().endsWith('.wav') ? 'fa-file-audio-o' : label.toLowerCase().endsWith('.js') || label.toLowerCase().endsWith('.html') || label.toLowerCase().endsWith('.css') || label.toLowerCase().endsWith('.py') ? 'fa-file-code-o' : 'fa-file-o')}' style='margin-right: 5px; color: ${type === 'folder' ? '#f39c12' : (label.toLowerCase().endsWith('.pdf') ? '#e74c3c' : label.toLowerCase().endsWith('.doc') || label.toLowerCase().endsWith('.docx') ? '#2980b9' : label.toLowerCase().endsWith('.xls') || label.toLowerCase().endsWith('.xlsx') ? '#27ae60' : label.toLowerCase().endsWith('.ppt') || label.toLowerCase().endsWith('.pptx') ? '#e67e22' : label.toLowerCase().endsWith('.jpg') || label.toLowerCase().endsWith('.jpeg') || label.toLowerCase().endsWith('.png') || label.toLowerCase().endsWith('.gif') ? '#9b59b6' : label.toLowerCase().endsWith('.zip') || label.toLowerCase().endsWith('.rar') || label.toLowerCase().endsWith('.7z') ? '#95a5a6' : label.toLowerCase().endsWith('.mp4') || label.toLowerCase().endsWith('.avi') || label.toLowerCase().endsWith('.mov') ? '#e74c3c' : label.toLowerCase().endsWith('.mp3') || label.toLowerCase().endsWith('.wav') ? '#1abc9c' : label.toLowerCase().endsWith('.js') ? '#f1c40f' : label.toLowerCase().endsWith('.html') ? '#e67e22' : label.toLowerCase().endsWith('.css') ? '#3498db' : label.toLowerCase().endsWith('.py') ? '#2ecc71' : '#7f8c8d')};'></i>"
                           },
                           {
                             "type": "button",
                             "label": "${label}",
                             "level": "link",
                             "size": "sm",
                             "actionType": "dialog",
                             "visibleOn": "${type === 'folder'}",
                             "dialog": {
                               "title": "${label} - 文件列表",
                               "size": "lg",
                               "body": {
                                 "type": "service",
                                 "api": {
                                   "url": "/remote_file/list_project_files",
                                   "method": "get",
                                   "data": {
                                     "project_name": "${currentProject}",
                                     "sub_path": "${value}"
                                   },
                                   "adaptor": `
                                     const projectName = api.query.project_name || api.data.project_name;
                                     const subPath = api.query.sub_path || api.data.sub_path || '';
                                     return {
                                       status: 0,
                                       data: {
                                         items: payload.map(item => ({
                                           label: item.name,
                                           value: subPath ? subPath + '/' + item.name : item.name,
                                           type: item.is_dir ? 'folder' : 'file',
                                           size: item.is_dir ? '-' : (item.size / 1024).toFixed(1) + ' KB',
                                           last_modified: new Date(Number(item.last_modified) * 1000).toLocaleString(),
                                           currentProject: projectName
                                         }))
                                       }
                                     };
                                   `
                                 },
                                 "body": [
                                   {
                                     "type": "table",
                                     "source": "${items}",
                                     "columns": [
                                       {
                                          "name": "label",
                                          "label": "文件名",
                                          "type": "container",
                                          "body": [
                                            {
                                              "type": "tpl",
                                              "tpl": "<i class='fa ${type === 'folder' ? 'fa-folder' : (label.toLowerCase().endsWith('.pdf') ? 'fa-file-pdf-o' : label.toLowerCase().endsWith('.doc') || label.toLowerCase().endsWith('.docx') ? 'fa-file-word-o' : label.toLowerCase().endsWith('.xls') || label.toLowerCase().endsWith('.xlsx') ? 'fa-file-excel-o' : label.toLowerCase().endsWith('.ppt') || label.toLowerCase().endsWith('.pptx') ? 'fa-file-powerpoint-o' : label.toLowerCase().endsWith('.jpg') || label.toLowerCase().endsWith('.jpeg') || label.toLowerCase().endsWith('.png') || label.toLowerCase().endsWith('.gif') ? 'fa-file-image-o' : label.toLowerCase().endsWith('.zip') || label.toLowerCase().endsWith('.rar') || label.toLowerCase().endsWith('.7z') ? 'fa-file-archive-o' : label.toLowerCase().endsWith('.mp4') || label.toLowerCase().endsWith('.avi') || label.toLowerCase().endsWith('.mov') ? 'fa-file-video-o' : label.toLowerCase().endsWith('.mp3') || label.toLowerCase().endsWith('.wav') ? 'fa-file-audio-o' : label.toLowerCase().endsWith('.js') || label.toLowerCase().endsWith('.html') || label.toLowerCase().endsWith('.css') || label.toLowerCase().endsWith('.py') ? 'fa-file-code-o' : 'fa-file-o')}' style='margin-right: 5px; color: ${type === 'folder' ? '#f39c12' : (label.toLowerCase().endsWith('.pdf') ? '#e74c3c' : label.toLowerCase().endsWith('.doc') || label.toLowerCase().endsWith('.docx') ? '#2980b9' : label.toLowerCase().endsWith('.xls') || label.toLowerCase().endsWith('.xlsx') ? '#27ae60' : label.toLowerCase().endsWith('.ppt') || label.toLowerCase().endsWith('.pptx') ? '#e67e22' : label.toLowerCase().endsWith('.jpg') || label.toLowerCase().endsWith('.jpeg') || label.toLowerCase().endsWith('.png') || label.toLowerCase().endsWith('.gif') ? '#9b59b6' : label.toLowerCase().endsWith('.zip') || label.toLowerCase().endsWith('.rar') || label.toLowerCase().endsWith('.7z') ? '#95a5a6' : label.toLowerCase().endsWith('.mp4') || label.toLowerCase().endsWith('.avi') || label.toLowerCase().endsWith('.mov') ? '#e74c3c' : label.toLowerCase().endsWith('.mp3') || label.toLowerCase().endsWith('.wav') ? '#1abc9c' : label.toLowerCase().endsWith('.js') ? '#f1c40f' : label.toLowerCase().endsWith('.html') ? '#e67e22' : label.toLowerCase().endsWith('.css') ? '#3498db' : label.toLowerCase().endsWith('.py') ? '#2ecc71' : '#7f8c8d')};'></i>"
                                            },
                                            {
                                              "type": "button",
                                              "label": "${label}",
                                              "level": "link",
                                              "size": "sm",
                                              "actionType": "dialog",
                                              "visibleOn": "${type === 'folder'}",
                                              "dialog": {
                                                "title": "${label} - 文件列表",
                                                "size": "lg",
                                                "body": {
                                                  "type": "service",
                                                  "api": {
                                                    "url": "/remote_file/list_project_files",
                                                    "method": "get",
                                                    "data": {
                                                      "project_name": "${currentProject}",
                                                      "sub_path": "${value}"
                                                    },
                                                    "adaptor": `
                                                      const projectName = api.query.project_name || api.data.project_name;
                                                      const subPath = api.query.sub_path || api.data.sub_path || '';
                                                      return {
                                                        status: 0,
                                                        data: {
                                                          items: payload.map(item => ({
                                                            label: item.name,
                                                            value: subPath ? subPath + '/' + item.name : item.name,
                                                            type: item.is_dir ? 'folder' : 'file',
                                                            size: item.is_dir ? '-' : (item.size / 1024).toFixed(1) + ' KB',
                                                            last_modified: new Date(Number(item.last_modified) * 1000).toLocaleString(),
                                                            currentProject: projectName
                                                          }))
                                                        }
                                                      };
                                                    `
                                                  },
                                                  "body": [
                                                    {
                                                      "type": "table",
                                                      "source": "${items}",
                                                      "columns": [
                                                        {
                                                          "name": "label",
                                                          "label": "文件名",
                                                          "type": "tpl",
                                                          "tpl": "<i class='fa ${type === 'folder' ? 'fa-folder' : (label.toLowerCase().endsWith('.pdf') ? 'fa-file-pdf-o' : label.toLowerCase().endsWith('.doc') || label.toLowerCase().endsWith('.docx') ? 'fa-file-word-o' : label.toLowerCase().endsWith('.xls') || label.toLowerCase().endsWith('.xlsx') ? 'fa-file-excel-o' : label.toLowerCase().endsWith('.ppt') || label.toLowerCase().endsWith('.pptx') ? 'fa-file-powerpoint-o' : label.toLowerCase().endsWith('.jpg') || label.toLowerCase().endsWith('.jpeg') || label.toLowerCase().endsWith('.png') || label.toLowerCase().endsWith('.gif') ? 'fa-file-image-o' : label.toLowerCase().endsWith('.zip') || label.toLowerCase().endsWith('.rar') || label.toLowerCase().endsWith('.7z') ? 'fa-file-archive-o' : label.toLowerCase().endsWith('.mp4') || label.toLowerCase().endsWith('.avi') || label.toLowerCase().endsWith('.mov') ? 'fa-file-video-o' : label.toLowerCase().endsWith('.mp3') || label.toLowerCase().endsWith('.wav') ? 'fa-file-audio-o' : label.toLowerCase().endsWith('.js') || label.toLowerCase().endsWith('.html') || label.toLowerCase().endsWith('.css') || label.toLowerCase().endsWith('.py') ? 'fa-file-code-o' : 'fa-file-o')}' style='margin-right: 5px; color: ${type === 'folder' ? '#f39c12' : (label.toLowerCase().endsWith('.pdf') ? '#e74c3c' : label.toLowerCase().endsWith('.doc') || label.toLowerCase().endsWith('.docx') ? '#2980b9' : label.toLowerCase().endsWith('.xls') || label.toLowerCase().endsWith('.xlsx') ? '#27ae60' : label.toLowerCase().endsWith('.ppt') || label.toLowerCase().endsWith('.pptx') ? '#e67e22' : label.toLowerCase().endsWith('.jpg') || label.toLowerCase().endsWith('.jpeg') || label.toLowerCase().endsWith('.png') || label.toLowerCase().endsWith('.gif') ? '#9b59b6' : label.toLowerCase().endsWith('.zip') || label.toLowerCase().endsWith('.rar') || label.toLowerCase().endsWith('.7z') ? '#95a5a6' : label.toLowerCase().endsWith('.mp4') || label.toLowerCase().endsWith('.avi') || label.toLowerCase().endsWith('.mov') ? '#e74c3c' : label.toLowerCase().endsWith('.mp3') || label.toLowerCase().endsWith('.wav') ? '#1abc9c' : label.toLowerCase().endsWith('.js') ? '#f1c40f' : label.toLowerCase().endsWith('.html') ? '#e67e22' : label.toLowerCase().endsWith('.css') ? '#3498db' : label.toLowerCase().endsWith('.py') ? '#2ecc71' : '#7f8c8d')};'></i>${label}"
                                                        },
                                                        {
                                                          "name": "last_modified",
                                                          "label": "修改时间",
                                                          "type": "tpl",
                                                          "tpl": "${last_modified}"
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                }
                                              },
                                              "visibleOn": "${type === 'folder'}"
                                            },
                                            {
                                              "type": "tpl",
                                              "tpl": "${label}",
                                              "visibleOn": "${type === 'file'}"
                                            }
                                          ],
                                          "style": {
                                            "display": "flex",
                                            "alignItems": "center"
                                          }
                                        },
                                       {
                                         "name": "last_modified",
                                         "label": "修改时间",
                                         "type": "tpl",
                                         "tpl": "${last_modified}"
                                       }
                                     ]
                                   }
                                 ]
                               }
                             }
                           },
                           {
                             "type": "tpl",
                             "tpl": "${label}",
                             "visibleOn": "${type === 'file'}"
                           }
                         ],
                         "style": {
                           "display": "flex",
                           "alignItems": "center"
                         }
                       },
                      {
                        "name": "last_modified",
                        "label": "修改时间",
                        "type": "tpl",
                        "tpl": "${last_modified}"
                      }
                    ]
                  }
                ]
              }
            }
          }
        ]
      }
    ]
  };

  window.jsonpCallback && window.jsonpCallback(response);
})();
