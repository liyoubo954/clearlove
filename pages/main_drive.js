(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "新增主驱动运行时间",
        "icon": "fa fa-plus",
        "level": "primary",
        "className": "m-b-sm",
        "actionType": "dialog",
        "dialog": {
          "title": "新增主驱动运行时间",
          "body": {
            "type": "form",
            "api": {
              "method": "post",
              "url": "/main_drive/main_drive",
              "messages": {
                "success": "添加成功",
                "failed": "添加失败"
              }
            },
            "body": [
              {
                "type": "input-text",
                "name": "shield_number",
                "label": "盾构机编号",
                "required": true
              },
              {
                "type": "input-text",
                "name": "segment_outside_diameter",
                "label": "管片外径",
                "required": true
              },
              {
                "type": "input-text",
                "name": "manufacturer",
                "label": "制造商",
                "required": true
              },
              {
                "type": "input-text",
                "name": "purchase_time",
                "label": "购置时间",
                "required": true
              },
              {
                "type": "input-text",
                "name": "participation_project",
                "label": "参加项目"
              },
              {
                "type": "input-text",
                "name": "time_departure",
                "label": "始发时间"
              },
              {
                "type": "input-text",
                "name": "receipt_time",
                "label": "接收时间"
              },
              {
                "type": "input-text",
                "name": "design_length",
                "label": "设计长度"
              },
              {
                "type": "input-text",
                "name": "length_under_construction",
                "label": "已施工长度"
              },
              {
                "type": "input-text",
                "name": "cumulative_construction_length",
                "label": "累计施工长度"
              },
              {
                "type": "input-text",
                "name": "main_drive_running_time",
                "label": "主驱动运行时间"
              },
              {
                "type": "input-text",
                "name": "cumulative_running_time",
                "label": "累计运行时间"
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
          "url": "/main_drive/main_drive_list",
          "method": "get",
          "dataType": "json"
        },
        "headerToolbar": [
          {
            "type": "tpl",
            "tpl": "<div class='header-title'><i class='fa fa-cog'></i> 主驱动运行时间统计</div>"
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
              "name": "shield_number",
              "label": "盾构机编号",
              "placeholder": "请输入盾构机编号进行查询"
            },
            {
              "type": "input-text",
              "name": "manufacturer",
              "label": "制造商",
              "placeholder": "请输入制造商进行查询"
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
                "actionType": "dialog",
                "dialog": {
                  "title": "修改主驱动运行时间",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/main_drive/update_main_drive",
                      "messages": {
                        "success": "更新成功",
                        "failed": "更新失败"
                      }
                    },
                    "body": [
                      {"type": "hidden", "name": "id"},
                      {"type": "input-text", "name": "shield_number", "label": "盾构机编号", "required": true},
                      {"type": "input-text", "name": "segment_outside_diameter", "label": "管片外径", "required": true},
                      {"type": "input-text", "name": "manufacturer", "label": "制造商", "required": true},
                      {"type": "input-text", "name": "purchase_time", "label": "购置时间", "required": true},
                      {"type": "input-text", "name": "participation_project", "label": "参加项目"},
                      {"type": "input-text", "name": "time_departure", "label": "始发时间"},
                      {"type": "input-text", "name": "receipt_time", "label": "接收时间"},
                      {"type": "input-text", "name": "design_length", "label": "设计长度"},
                      {"type": "input-text", "name": "length_under_construction", "label": "已施工长度"},
                      {"type": "input-text", "name": "cumulative_construction_length", "label": "累计施工长度"},
                      {"type": "input-text", "name": "main_drive_running_time", "label": "主驱动运行时间"},
                      {"type": "input-text", "name": "cumulative_running_time", "label": "累计运行时间"},
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
                  "url": "/main_drive/delete_main_drive/${id}"
                },
                "messages": {
                  "success": "删除成功",
                  "failed": "删除失败"
                }
              }
            ]
          },
          { "name": "id","label": "编号","type": "number", "width": 80 },
          { "name": "shield_number", "label": "盾构机编号", "type": "text", "width": 120 },
          { "name": "segment_outside_diameter", "label": "管片外径", "type": "text", "width": 100 },
          { "name": "manufacturer", "label": "制造商", "type": "text", "width": 120 },
          { "name": "purchase_time", "label": "购置时间", "type": "text", "width": 120 },
          { "name": "participation_project", "label": "参加项目", "type": "text", "width": 150 },
          { "name": "time_departure", "label": "始发时间", "type": "text", "width": 120 },
          { "name": "receipt_time", "label": "接收时间", "type": "text", "width": 120 },
          { "name": "design_length", "label": "设计长度", "type": "text", "width": 100 },
          { "name": "length_under_construction", "label": "已施工长度", "type": "text", "width": 120 },
          { "name": "cumulative_construction_length", "label": "累计施工长度", "type": "text", "width": 120 },
          { "name": "main_drive_running_time", "label": "主驱动运行时间", "type": "text", "width": 120 },
          { "name": "cumulative_running_time", "label": "累计运行时间", "type": "text", "width": 120 },
          { "name": "remark", "label": "备注", "type": "text", "width": 200 }
        ]
      }
    ]
  };

  window.jsonpCallback && window.jsonpCallback(response);
})();