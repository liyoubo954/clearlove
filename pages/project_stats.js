(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "新增项目统计",
        "icon": "fa fa-plus",
        "level": "primary",
        "className": "m-b-sm",
        "actionType": "dialog",
        "dialog": {
          "title": "新增项目统计",
          "body": {
            "type": "form",
            "api": {
              "method": "post",
              "url": "/project_stats/project_stats",
              "messages": {
                "success": "添加成功",
                "failed": "添加失败"
              }
            },
            "body": [
              {
                "type": "input-text",
                "name": "project_name",
                "label": "项目名称",
                "required": true
              },
              {
                "type": "input-text",
                "name": "work_area",
                "label": "工区",
                "required": true
              },
              {
                "type": "input-text",
                "name": "bid_money",
                "label": "中标金额",
                "required": true
              },
              {
                "type": "input-text",
                "name": "bid_time",
                "label": "中标时间",
                "required": true
              },
              {
                "type": "input-text",
                "name": "finish_time",
                "label": "完工时间"
              },
              {
                "type": "input-text",
                "name": "tunnel_length",
                "label": "隧道长度"
              },
              {
                "type": "input-text",
                "name": "tube_outer_diameter",
                "label": "管片外径"
              },
              {
                "type": "input-text",
                "name": "through_waters",
                "label": "是否穿越水域"
              },
              {
                "type": "input-text",
                "name": "max_excavation_diameter",
                "label": "最大开挖直径"
              },
              {
                "type": "input-text",
                "name": "project_type",
                "label": "工程类型"
              },
              {
                "type": "input-text",
                "name": "job_schedule",
                "label": "工程进度"
              },
              {
                "type": "input-text",
                "name": "type",
                "label": "后构类型"
              },
              {
                "type": "input-text",
                "name": "company_name",
                "label": "单位名称"
              },
              {
                "type": "input-text",
                "name": "province",
                "label": "省份"
              },
              {
                "type": "input-text",
                "name": "remark",
                "label": "备注"
              },
              {
                "type": "input-text",
                "name": "pro_code",
                "label": "项目编码"
              },
              {
                "type": "input-text",
                "name": "sub_code",
                "label": "项目区间编码"
              },
              {
                "type": "input-text",
                "name": "through_assise",
                "label": "穿越地层"
              },
              {
                "type": "input-text",
                "name": "hydraulic_pressure",
                "label": "埋深水压"
              },
              {
                "type": "input-text",
                "name": "intension",
                "label": "衬砌强度"
              },
              {
                "type": "input-text",
                "name": "duct_piece",
                "label": "隧道管片"
              },
              {
                "type": "input-number",
                "name": "zone_id",
                "label": "项目区间id"
              },
              {
                "type": "input-number",
                "name": "shield_machine_id",
                "label": "盾构机ID"
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
          "url": "/project_stats/project_stats_list",
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
            "tpl": "<div class='header-title'><i class='fa fa-cog'></i> 大直径盾构项目统计</div>"
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
              "name": "project_name",
              "label": "项目名称",
              "placeholder": "请输入项目名称进行查询"
            },
            {
              "type": "input-text",
              "name": "work_area",
              "label": "工区",
              "placeholder": "请输入工区进行查询"
            },
            {
              "type": "input-text",
              "name": "pro_code",
              "label": "项目编码",
              "placeholder": "请输入项目编码进行查询"
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
                  "title": "修改项目统计",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/project_stats/update_project_stats",
                      "messages": {
                        "success": "更新成功",
                        "failed": "更新失败"
                      }
                    },
                    "body": [
                      {"type": "hidden", "name": "id"},
                      {"type": "input-text", "name": "project_name", "label": "项目名称", "required": true},
                      {"type": "input-text", "name": "work_area", "label": "工区", "required": true},
                      {"type": "input-text", "name": "bid_money", "label": "中标金额"},
                      {"type": "input-text", "name": "bid_time", "label": "中标时间"},
                      {"type": "input-text", "name": "finish_time", "label": "完工时间"},
                      {"type": "input-text", "name": "tunnel_length", "label": "隧道长度"},
                      {"type": "input-text", "name": "tube_outer_diameter", "label": "管片外径"},
                      {"type": "input-text", "name": "through_waters", "label": "是否穿越水域"},
                      {"type": "input-text", "name": "max_excavation_diameter", "label": "最大开挖直径"},
                      {"type": "input-text", "name": "project_type", "label": "工程类型"},
                      {"type": "input-text", "name": "job_schedule", "label": "工程进度"},
                      {"type": "input-text", "name": "type", "label": "后构类型"},
                      {"type": "input-text", "name": "company_name", "label": "单位名称"},
                      {"type": "input-text", "name": "province", "label": "省份"},
                      {"type": "input-text", "name": "remark", "label": "备注"},
                      {"type": "input-text", "name": "pro_code", "label": "项目编码"},
                      {"type": "input-text", "name": "sub_code", "label": "项目区间编码"},
                      {"type": "input-text", "name": "through_assise", "label": "穿越地层"},
                      {"type": "input-text", "name": "hydraulic_pressure", "label": "埋深水压"},
                      {"type": "input-text", "name": "intension", "label": "衬砌强度"},
                      {"type": "input-text", "name": "duct_piece", "label": "隧道管片"},
                      {"type": "input-number", "name": "zone_id", "label": "项目区间id"},
                      {"type": "input-number", "name": "shield_machine_id", "label": "盾构机ID"}
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
                  "url": "/project_stats/delete_project_stats/${id}"
                },
                "messages": {
                  "success": "删除成功",
                  "failed": "删除失败"
                }
              }
            ]
          },
          { "name": "id","label": "编号","type": "number", "width": 80 },
          { "name": "project_name", "label": "项目名称", "type": "text", "width": 150 },
          { "name": "work_area", "label": "工区", "type": "text", "width": 100 },
          { "name": "bid_money", "label": "中标金额", "type": "text", "width": 120 },
          { "name": "bid_time", "label": "中标时间", "type": "text", "width": 120 },
          { "name": "finish_time", "label": "完工时间", "type": "text", "width": 120 },
          { "name": "tunnel_length", "label": "隧道长度", "type": "text", "width": 100 },
          { "name": "tube_outer_diameter", "label": "管片外径", "type": "text", "width": 100 },
          { "name": "through_waters", "label": "是否穿越水域", "type": "text", "width": 120 },
          { "name": "max_excavation_diameter", "label": "最大开挖直径", "type": "text", "width": 120 },
          { "name": "project_type", "label": "工程类型", "type": "text", "width": 100 },
          { "name": "job_schedule", "label": "工程进度", "type": "text", "width": 100 },
          { "name": "type", "label": "后构类型", "type": "text", "width": 100 },
          { "name": "company_name", "label": "单位名称", "type": "text", "width": 150 },
          { "name": "province", "label": "省份", "type": "text", "width": 100 },
          { "name": "remark", "label": "备注", "type": "text", "width": 200 },
          { "name": "pro_code", "label": "项目编码", "type": "text", "width": 120 },
          { "name": "sub_code", "label": "项目区间编码", "type": "text", "width": 120 },
          { "name": "through_assise", "label": "穿越地层", "type": "text", "width": 120 },
          { "name": "hydraulic_pressure", "label": "埋深水压", "type": "text", "width": 100 },
          { "name": "intension", "label": "衬砌强度", "type": "text", "width": 100 },
          { "name": "duct_piece", "label": "隧道管片", "type": "text", "width": 100 },
          { "name": "zone_id", "label": "项目区间id", "type": "number", "width": 100 },
          { "name": "shield_machine_id", "label": "盾构机ID", "type": "number", "width": 100 }
        ]
      }
    ]
  };

  window.jsonpCallback && window.jsonpCallback(response);
})();