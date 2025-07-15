(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "新增施工进度",
        "icon": "fa fa-plus",
        "level": "primary",
        "className": "m-b-sm",
        "actionType": "dialog",
        "dialog": {
          "title": "新增施工进度",
          "body": {
            "type": "form",
            "api": {
              "method": "post",
              "url": "/construction_progress/progress",
              "messages": {
                "success": "添加成功",
                "failed": "添加失败"
              }
            },
            "body": [
              {
                "type": "input-text",
                "name": "shield_id",
                "label": "盾构机编号",
                "required": true
              },
              {
                "type": "input-text",
                "name": "pro_name",
                "label": "区间名称",
                "required": true
              },
              {
                "type": "input-text",
                "name": "interval_length",
                "label": "区间长度"
              },
              {
                "type": "input-date",
                "name": "start_time",
                "label": "始发时间",
                "required": true,
                "format": "YYYY-MM-DD"
              },
              {
                "type": "input-text",
                "name": "today_ring",
                "label": "今日进度-环"
              },
              {
                "type": "input-text",
                "name": "today_schedule",
                "label": "今日进度-m"
              },
              {
                "type": "input-text",
                "name": "plan_ring",
                "label": "计划进度-环"
              },
              {
                "type": "input-text",
                "name": "plan_schedule",
                "label": "计划进度-m"
              },
              {
                "type": "input-text",
                "name": "accumulate_ring",
                "label": "开累进度-环"
              },
              {
                "type": "input-number",
                "name": "accumulate_day",
                "label": "累计天数-天"
              },
              {
                "type": "input-text",
                "name": "avg_schedule",
                "label": "平均日进度-m"
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
          "url": "/construction_progress/progress_list",
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
            "tpl": "<div class='header-title'><i class='fa fa-list'></i> 施工进度报表</div>"
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
              "name": "shield_id",
              "label": "盾构机编号",
              "placeholder": "请输入盾构机编号进行查询"
            },
            {
              "type": "input-text",
              "name": "pro_name",
              "label": "区间名称",
              "placeholder": "请输入区间名称进行查询"
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
                  "title": "修改施工进度",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/construction_progress/update_progress",
                      "messages": {
                        "success": "更新成功",
                        "failed": "更新失败"
                      }
                    },
                    "body": [
                      {"type": "hidden", "name": "id"},
                      {"type": "input-text", "name": "shield_id", "label": "盾构机编号", "required": true},
                      {"type": "input-text", "name": "pro_name", "label": "区间名称", "required": true},
                      {"type": "input-text", "name": "interval_length", "label": "区间长度"},
                      {"type": "input-date", "name": "start_time", "label": "始发时间", "required": true, "format": "YYYY-MM-DD"},
                      {"type": "input-text", "name": "today_ring", "label": "今日进度-环"},
                      {"type": "input-text", "name": "today_schedule", "label": "今日进度-m"},
                      {"type": "input-text", "name": "plan_ring", "label": "计划进度-环"},
                      {"type": "input-text", "name": "plan_schedule", "label": "计划进度-m"},
                      {"type": "input-text", "name": "accumulate_ring", "label": "开累进度-环"},
                      {"type": "input-number", "name": "accumulate_day", "label": "累计天数-天"},
                      {"type": "input-text", "name": "avg_schedule", "label": "平均日进度-m"}
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
            "url": "/construction_progress/delete_progress/${id}"
          },
                "messages": {
                  "success": "删除成功",
                  "failed": "删除失败"
                }
              }
            ]
          },
          { "name": "id","label": "编号", "type": "number", "width": 80 },
          { "name": "shield_id", "label": "盾构机编号", "type": "text", "width": 120 },
          { "name": "pro_name", "label": "区间名称", "type": "text", "width": 150 },
          { "name": "interval_length", "label": "区间长度", "type": "text", "width": 100 },
          { "name": "start_time", "label": "始发时间", "type": "date", "width": 120 },
          { "name": "today_ring", "label": "今日进度-环", "type": "text", "width": 100 },
          { "name": "today_schedule", "label": "今日进度-m", "type": "text", "width": 100 },
          { "name": "plan_ring", "label": "计划进度-环", "type": "text", "width": 100 },
          { "name": "plan_schedule", "label": "计划进度-m", "type": "text", "width": 100 },
          { "name": "accumulate_ring", "label": "开累进度-环", "type": "text", "width": 100 },
          { "name": "accumulate_day", "label": "累计天数-天", "type": "number", "width": 100 },
          { "name": "avg_schedule", "label": "平均日进度-m", "type": "text", "width": 100 }
        ]
      }
    ]
  };

  window.jsonpCallback && window.jsonpCallback(response);
})();