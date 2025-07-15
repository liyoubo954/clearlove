(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "新增工程参数",
        "icon": "fa fa-plus",
        "level": "primary",
        "className": "m-b-sm",
        "actionType": "dialog",
        "dialog": {
          "title": "新增工程参数",
          "body": {
            "type": "form",
            "api": {
              "method": "post",
              "url": "/engineering_params/engineering_params",
              "messages": {
                "success": "添加成功",
                "failed": "添加失败"
              }
            },
            "body": [
              {
                "type": "input-text",
                "name": "instanceid",
                "label": "流程id",
                "required": true
              },
              {
                "type": "input-text",
                "name": "sub_code",
                "label": "工点编码",
                "required": true
              },
              {
                "type": "input-text",
                "name": "pro_code",
                "label": "项目编码",
                "required": true
              },
              {
                "type": "input-text",
                "name": "pro_name",
                "label": "项目名称",
                "required": true
              },
              {
                "type": "input-text",
                "name": "connect_key",
                "label": "盾构机编号"
              },
              {
                "type": "input-number",
                "name": "max_diameter",
                "label": "最大开挖直径"
              },
              {
                "type": "input-number",
                "name": "rube_outerdiameter",
                "label": "管片外径"
              },
              {
                "type": "input-number",
                "name": "rube_innerdiameter",
                "label": "管片内径"
              },
              {
                "type": "input-number",
                "name": "rube_thick",
                "label": "管片厚度"
              },
              {
                "type": "input-number",
                "name": "rube_width",
                "label": "管片环宽"
              },
              {
                "type": "input-text",
                "name": "geocondition",
                "label": "地质情况"
              },
              {
                "type": "input-text",
                "name": "remark",
                "label": "备注"
              }
            ]
          }
        }
      },
      {
        "type": "crud",
        "syncLocation": false,
        "resizable": true,
        "columnsTogglable": true,
        "className": "table-db m-b-none",
        "tableClassName": "table-cell-nowrap",
        "api": {
          "url": "/engineering_params/engineering_params_list",
          "method": "get",
          "dataType": "json",
          "adaptor": function (payload) {
            return {
              status: payload.status,
              msg: payload.msg,
              data: {
                items: payload.data && payload.data.items ? payload.data.items : [],
                total: payload.data && payload.data.total ? payload.data.total : 0
              }
            };
          }
        },
        "headerToolbar": [
          {
            "type": "tpl",
            "tpl": "<div class='header-title'><i class='fa fa-cog'></i> 工程参数管理</div>"
          },
          "export-excel",
          {
            "type": "reload",
            "icon": "fa fa-refresh",
            "tooltip": "刷新数据",
            "tooltipPlacement": "top",
            "level": "link"
          }
        ],
        "filter": {
          "title": "查询条件",
          "submitText": "查询",
          "body": [
            {
              "type": "input-text",
              "name": "instanceid",
              "label": "流程id",
              "placeholder": "请输入流程id进行查询"
            },
            {
              "type": "input-text",
              "name": "sub_code",
              "label": "工点编码",
              "placeholder": "请输入工点编码进行查询"
            },
            {
              "type": "input-text",
              "name": "pro_code",
              "label": "项目编码",
              "placeholder": "请输入项目编码进行查询"
            },
            {
              "type": "input-text",
              "name": "pro_name",
              "label": "项目名称",
              "placeholder": "请输入项目名称进行查询"
            }
          ]
        },
        "columns": [
          {
            "type": "operation",
            "label": "操作",
            "width": 80,
            "fixed": "right",
            "buttons": [
              {
                "type": "button",
                "icon": "fa fa-pencil",
                "tooltip": "修改",
                "level": "link",
                "actionType": "drawer",
                "drawer": {
                  "position": "right",
                  "size": "md",
                  "title": "修改工程参数",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/engineering_params/update_engineering_params",
                      "messages": {
                        "success": "更新成功",
                        "failed": "更新失败"
                      }
                    },
                    "body": [
                      {"type": "hidden", "name": "id"},
                      {"type": "input-number", "name": "instanceid", "label": "流程id", "required": true},
                      {"type": "input-text", "name": "sub_code", "label": "工点编码", "required": true},
                      {"type": "input-text", "name": "pro_code", "label": "项目编码", "required": true},
                      {"type": "input-text", "name": "pro_name", "label": "项目名称", "required": true},
                      {"type": "input-text", "name": "connect_key", "label": "盾构机编号"},
                      {"type": "input-number", "name": "max_diameter", "label": "最大开挖直径"},
                      {"type": "input-number", "name": "rube_outerdiameter", "label": "管片外径"},
                      {"type": "input-number", "name": "rube_innerdiameter", "label": "管片内径"},
                      {"type": "input-number", "name": "rube_thick", "label": "管片厚度"},
                      {"type": "input-number", "name": "rube_width", "label": "管片环宽"},
                      {"type": "input-text", "name": "geocondition", "label": "地质情况"},
                      {"type": "input-text", "name": "remark", "label": "备注"}
                    ]
                  }
                }
              },
              {
                "type": "button",
                "icon": "fa fa-times text-danger",
                "actionType": "ajax",
                "tooltip": "删除",
                "confirmText": "确定要删除该记录吗？",
                "api": {
                  "method": "delete",
                  "url": "/engineering_params/delete_engineering_params/${id}"
                },
                "messages": {
                  "success": "删除成功",
                  "failed": "删除失败"
                }
              }
            ]
          },
          { "name": "id","label": "编号","type": "number", "width": 80 },
          { "name": "instanceid", "label": "流程id", "type": "number", "width": 100 },
          { "name": "sub_code", "label": "工点编码", "type": "text", "width": 120 },
          { "name": "pro_code", "label": "项目编码", "type": "text", "width": 120 },
          { "name": "pro_name", "label": "项目名称", "type": "text", "width": 150 },
          { "name": "connect_key", "label": "盾构机编号", "type": "text", "width": 120 },
          { "name": "max_diameter", "label": "最大开挖直径", "type": "number", "width": 120 },
          { "name": "rube_outerdiameter", "label": "管片外径", "type": "number", "width": 100 },
          { "name": "rube_innerdiameter", "label": "管片内径", "type": "number", "width": 100 },
          { "name": "rube_thick", "label": "管片厚度", "type": "number", "width": 100 },
          { "name": "rube_width", "label": "管片环宽", "type": "number", "width": 100 },
          { "name": "geocondition", "label": "地质情况", "type": "text", "width": 150 },
          { "name": "remark", "label": "备注", "type": "text", "width": 200 }
        ]
      }
    ]
  };

  window.jsonpCallback && window.jsonpCallback(response);
})();