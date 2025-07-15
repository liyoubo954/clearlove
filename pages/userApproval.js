(function () {
    const response = {
        "type": "page",
        "body": [
            {
                "type": "crud",
                "api": {
                    "method": "get",
                    "url": "http://127.0.0.1:8010/api/user/approval/list", 
                    "dataType": "json"
                },
                "columns": [
                    {
                        "name": "username",
                        "label": "用户名",
                        "type": "text"
                    },
                    {
                        "name": "realName",
                        "label": "真实姓名",
                        "type": "text"
                    },
                    {
                        "name": "phone",
                        "label": "手机号",
                        "type": "text"
                    },
                    {
                        "name": "email",
                        "label": "邮箱",
                        "type": "text"
                    },
                    {
                        "name": "registerTime",
                        "label": "注册时间",
                        "type": "datetime"
                    },
                    {
                        "name": "status",
                        "label": "审核状态",
                        "type": "mapping",
                        "map": {
                            "0": "<span class='label label-warning'>待审核</span>",
                            "1": "<span class='label label-success'>已通过</span>",
                            "2": "<span class='label label-danger'>已拒绝</span>"
                        }
                    },
                    {
                        "type": "operation",
                        "label": "操作",
                        "buttons": [
                            {
                                "type": "button",
                                "label": "通过",
                                "level": "link",
                                "className": "text-success",
                                "actionType": "ajax",
                                "api": "/api/user/approve/${id}?status=1",
                                "confirmText": "确定要通过该用户申请吗？"
                            },
                            {
                                "type": "button",
                                "label": "拒绝",
                                "level": "link",
                                "className": "text-danger",
                                "actionType": "ajax",
                                "api": "/api/user/approve/${id}?status=2",
                                "confirmText": "确定要拒绝该用户申请吗？"
                            },
                            {
                                "type": "button",
                                "label": "详情",
                                "actionType": "dialog",
                                "dialog": {
                                    "title": "用户详情",
                                    "body": {
                                        "type": "form",
                                        "api": "/api/user/detail/${id}",
                                        "body": [
                                            {
                                                "type": "static",
                                                "name": "username",
                                                "label": "用户名"
                                            },
                                            {
                                                "type": "static",
                                                "name": "realName",
                                                "label": "真实姓名"
                                            },
                                            {
                                                "type": "static",
                                                "name": "idCard",
                                                "label": "身份证号"
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                ],
                "filter": {
                    "body": [
                        {
                            "type": "input-text",
                            "name": "keyword",
                            "placeholder": "请输入用户名/手机号查询"
                        },
                        {
                            "type": "select",
                            "name": "status",
                            "label": "审核状态",
                            "options": [
                                {"label": "全部", "value": ""},
                                {"label": "待审核", "value": "0"},
                                {"label": "已通过", "value": "1"},
                                {"label": "已拒绝", "value": "2"}
                            ]
                        },
                        {
                            "type": "button",
                            "actionType": "submit",
                            "label": "查询",
                            "level": "primary"
                        }
                    ]
                }
            }
        ]
    };
    window.jsonpCallback && window.jsonpCallback(response);
})();