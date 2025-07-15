(function () {
    const response = {
        "type": "page",
        "body": [
            // 新增用户按钮（仅管理员可见）
            {
                "type": "button",
                "label": "新增用户",
                "icon": "fa fa-plus",
                "level": "primary",
                "className": "m-b-sm",
                "actionType": "dialog",
                "dialog": {
                    "title": "新增用户表单",
                    "body": {
                        "type": "form",
                        "api": {
                            "method": "post",
                            "url": "/adminuser",
                            "messages": {
                                "success": "用户添加成功"
                            }
                        },
                        "body": [
                            {
                                "type": "input-text",
                                "name": "username",
                                "label": "用户名",
                                "required": true,
                                "placeholder": "请输入用户名"
                            },
                            {
                                "type": "input-password",
                                "name": "password",
                                "label": "密码",
                                "required": true,
                                "placeholder": "请输入密码"
                            },
                            {
                                "type": "input-text",
                                "name": "phone",
                                "label": "电话",
                                "placeholder": "请输入电话号码"
                            },
                            {
                                "type": "input-text",
                                "name": "remark",
                                "label": "备注",
                                "placeholder": "请输入备注信息"
                            }
                        ]
                    }
                }
            },
            // 新增文件上传按钮（与新增用户平行�?
                {
  "label": "文件上传",
  "type": "button",
  "actionType": "dialog",
  "level": "primary",
  "className": "m-b-sm m-l-sm",
  "dialog": {
    "title": "文件上传",
    "body": {
      "type": "form",
      "body": [
        {
          "type": "input-file",
          "label": "文件上传",
          "autoUpload": false,
          "mode": "inline",
          "receiver": "/file/uploadfiles",
          "proxy": true,
          "name": "file",
          "btnLabel": "文件上传",
          "multiple": true,
          "useChunk": false,
          "accept": "*",
          "drag": false,
          "onEvent": {
            "success": {
              "actions": [
                {
                  "actionType": "toast",
                  "args": {
                    "msgType": "info",
                    "msg": "「${event.data.path}」上传成功"
                  }
                }
              ]
            },
            "error": {
              "actions": [
                {
                  "actionType": "toast",
                  "args": {
                    "msgType": "error",
                    "msg": "文件上传失败，请检查文件类型或大小"
                  }
                }
              ]
            }
          }
        }
      ]
    }
  }
},

            // 用户列表表格
            {
                "type": "crud",
                "api": "/adminuser/page",
                "syncLocation": false,
                "autoGenerateFilter": true,
                "loadDataOnce": false,
                "headerToolbar": [
                    "export-excel"
                ],
                "exportExcel": {
                    "filename": "用户数据",
                    "columns": [
                        "id",
                        "username",
                        "password",
                        "phone",
                        "remark",
                        "createtime",
                        "updatetime"
                    ]
                },
                "columns": [
                    {
                        "name": "id",
                        "label": "ID",
                        "type": "text",
                        "width": 80
                    },
                    {
  "name": "username",
  "label": "用户名",
  "type": "text",
  "searchable": {
    "name": "username",     // 👈 这个很关键
    "type": "input-text",
    "placeholder": "请输入用户名"
  }
},
                    {
                        "name": "password",
                        "label": "密码",
                        "type": "password"
                    },
                    {
                        "name": "phone",
                        "label": "电话",
                        "type": "text",
                        "searchable": {
                            "name": "phone",
                            "type": "input-text",
                            "placeholder": "请输入电话号码"
                        }
                    },
                    {
                        "name": "remark",
                        "label": "备注",
                        "type": "text"
                    },
                    {
                        "name": "createtime",
                        "label": "创建时间",
                        "type": "datetime"
                    },
                    {
                        "name": "updatetime",
                        "label": "更新时间",
                        "type": "datetime"
                    },
                    {
                        "type": "operation",
                        "label": "操作",
                        "width": 150,
                        "buttons": [
                            {
                                "type": "button",
                                "icon": "fa fa-pencil",
                                "label": "修改",
                                "tooltip": "修改",
                                "actionType": "drawer",
                                "level": "link",
                                "drawer": {
                                    "position": "right",
                                    "size": "md",
                                    "title": "修改表单",
                                    "body": {
                                        "type": "form",
                                        "api": {
                                            "method": "put",
                                            "url": "/adminuser/${id}",
                                            "confirmText": "确定要修改该用户信息吗？",
                                            "messages": {
                                                "success": "用户信息更新成功",
                                                "failed": "用户信息更新失败"
                                            }
                                        },
                                        "body": [
                                            {
                                                "type": "hidden",
                                                "name": "id"
                                            },
                                            {
                                                "type": "input-text",
                                                "name": "username",
                                                "label": "用户名",
                                                "required": true
                                            },
                                            {
                                                "type": "input-password",
                                                "name": "password",
                                                "label": "密码",
                                                "required": true
                                            },
                                            {
                                                "type": "input-text",
                                                "name": "phone",
                                                "label": "电话",
                                                "placeholder": "请输入电话号码"
                                            },
                                            {
                                                "type": "input-text",
                                                "name": "remark",
                                                "label": "备注",
                                                "placeholder": "请输入备注信息"
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "type": "button",
                                "icon": "fa fa-times text-danger",
                                "label": "删除",
                                "actionType": "ajax",
                                "tooltip": "删除",
                                "level": "link",
                                "confirmText": "确定要删除该用户吗？删除后数据将无法恢复",
                                "api": "/adminuser/${id}",
                                "messages": {
                                    "success": "删除成功",
                                    "failed": "删除失败"
                                },
                                "reload": "crud"
                            }
                        ]
                    }
                ],
                "requestAdaptor": function (api) {
                    console.log("crud请求信息:", api);
                    return api;
                }
            }
        ]
    };

    window.jsonpCallback && window.jsonpCallback(response);
})();