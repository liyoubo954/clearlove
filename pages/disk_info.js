(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "新增刀盘信息",
        "icon": "fa fa-plus",
        "level": "primary",
        "className": "m-b-sm",
        "actionType": "dialog",
        "dialog": {
          "title": "新增刀盘信息",
          "body": {
            "type": "form",
            "api": {
              "method": "post",
              "url": "/disk_info/disk_info",
              "messages": {
                "success": "添加成功",
                "failed": "添加失败"
              }
            },
            "body": [
              {
                "type": "input-text",
                "name": "CONNECT_KEY",
                "label": "盾构机编号",
                "required": true
              },
              {
                "type": "input-text",
                "name": "DISK_TYPE",
                "label": "刀盘型号"
              },
              {
                "type": "input-text",
                "name": "KNIFE_DISTANCE",
                "label": "刀间距"
              },
              {
                "type": "input-text",
                "name": "CUTTER_HEIGHT_DIFFERENCE",
                "label": "刀高差"
              },
              {
                "type": "input-text",
                "name": "CHANGE_LOG",
                "label": "换刀记录"
              },
              {
                "type": "input-text",
                "name": "KNIFE_STATUS",
                "label": "刀具状态"
              },
              {
                "type": "input-text",
                "name": "ABRASION",
                "label": "磨损量"
              },
              {
                "type": "input-text",
                "name": "CUTTER_HOB",
                "label": "滚刀"
              },
              {
                "type": "input-text",
                "name": "GD_CC",
                "label": "滚刀尺寸"
              },
              {
                "type": "input-text",
                "name": "CUT_KNIFE",
                "label": "切刀"
              },
              {
                "type": "input-text",
                "name": "CUT_KNIFE_HEIGHT",
                "label": "切刀刀高"
              },
              {
                "type": "input-text",
                "name": "LACING_KNIFE",
                "label": "撕裂刀"
              },
              {
                "type": "input-text",
                "name": "LACING_KNIFE_HEIGHT",
                "label": "撕裂刀刀高"
              },
              {
                "type": "input-datetime",
                "name": "CREATE_TIME",
                "label": "创建时间",
                "format": "YYYY-MM-DD HH:mm:ss",
                "inputFormat": "YYYY-MM-DD HH:mm:ss",
                "timeFormat": "HH:mm:ss",
                "value": "${now()}"
              },
              {
                "type": "input-text",
                "name": "CREATE_BY",
                "label": "创建人"
              },
              {
                "type": "input-text",
                "name": "KNIFE_TYPE",
                "label": "刀具类型"
              },
              {
                "type": "input-text",
                "name": "KNIFE_LAYOUT",
                "label": "刀具轨迹布局"
              },
              {
                "type": "input-text",
                "name": "DP_ZTL",
                "label": "刀盘总推力"
              },
              {
                "type": "input-text",
                "name": "DP_NJ",
                "label": "刀盘扭矩"
              },
              {
                "type": "input-text",
                "name": "DP_ZS",
                "label": "刀盘转速"
              },
              {
                "type": "input-text",
                "name": "DP_GRD",
                "label": "刀盘贯入度"
              },
              {
                "type": "input-text",
                "name": "DP_ZJCL",
                "label": "刀盘总接触力"
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
          "url": "/disk_info/disk_info_list",
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
            "tpl": "<div class='header-title'><i class='fa fa-cog'></i> 刀盘信息管理</div>"
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
              "name": "CONNECT_KEY",
              "label": "盾构机编号",
              "placeholder": "请输入盾构机编号进行查询"
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
                  "title": "修改刀盘信息",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/disk_info/update_disk_info",
                      "messages": {
                        "success": "更新成功",
                        "failed": "更新失败"
                      }
                    },
                    "body": [
                      {"type": "hidden", "name": "ID"},
                      {"type": "input-text", "name": "CONNECT_KEY", "label": "盾构机编号", "required": true},
                      {"type": "input-text", "name": "DISK_TYPE", "label": "刀盘型号"},
                      {"type": "input-text", "name": "KNIFE_DISTANCE", "label": "刀间距"},
                      {"type": "input-text", "name": "CUTTER_HEIGHT_DIFFERENCE", "label": "刀高差"},
                      {"type": "input-text", "name": "CHANGE_LOG", "label": "换刀记录"},
                      {"type": "input-text", "name": "KNIFE_STATUS", "label": "刀具状态"},
                      {"type": "input-text", "name": "ABRASION", "label": "磨损量"},
                      {"type": "input-text", "name": "CUTTER_HOB", "label": "滚刀"},
                      {"type": "input-text", "name": "GD_CC", "label": "滚刀尺寸"},
                      {"type": "input-text", "name": "CUT_KNIFE", "label": "切刀"},
                      {"type": "input-text", "name": "CUT_KNIFE_HEIGHT", "label": "切刀刀高"},
                      {"type": "input-text", "name": "LACING_KNIFE", "label": "撕裂刀"},
                      {"type": "input-text", "name": "LACING_KNIFE_HEIGHT", "label": "撕裂刀刀高"},
                      {"type": "input-datetime", "name": "CREATE_TIME", "label": "创建时间"},
                      {"type": "input-text", "name": "CREATE_BY", "label": "创建人"},
                      {"type": "input-text", "name": "KNIFE_TYPE", "label": "刀具类型"},
                      {"type": "input-text", "name": "KNIFE_LAYOUT", "label": "刀具轨迹布局"},
                      {"type": "input-text", "name": "DP_ZTL", "label": "刀盘总推力"},
                      {"type": "input-text", "name": "DP_NJ", "label": "刀盘扭矩"},
                      {"type": "input-text", "name": "DP_ZS", "label": "刀盘转速"},
                      {"type": "input-text", "name": "DP_GRD", "label": "刀盘贯入度"},
                      {"type": "input-text", "name": "DP_ZJCL", "label": "刀盘总接触力"}
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
                  "url": "/disk_info/delete_disk_info/${ID}"
                },
                "messages": {
                  "success": "删除成功",
                  "failed": "删除失败"
                }
              }
            ]
          },
          { "name": "ID","label": "编号","type": "number", "width": 80 },
          { "name": "CONNECT_KEY", "label": "盾构机编号", "type": "text", "width": 120 },
          { "name": "DISK_TYPE", "label": "刀盘型号", "type": "text", "width": 120 },
          { "name": "KNIFE_DISTANCE", "label": "刀间距", "type": "text", "width": 100 },
          { "name": "CUTTER_HEIGHT_DIFFERENCE", "label": "刀高差", "type": "text", "width": 100 },
          { "name": "CHANGE_LOG", "label": "换刀记录", "type": "text", "width": 120 },
          { "name": "KNIFE_STATUS", "label": "刀具状态", "type": "text", "width": 100 },
          { "name": "ABRASION", "label": "磨损量", "type": "text", "width": 100 },
          { "name": "CUTTER_HOB", "label": "滚刀", "type": "text", "width": 100 },
          { "name": "GD_CC", "label": "滚刀尺寸", "type": "text", "width": 100 },
          { "name": "CUT_KNIFE", "label": "切刀", "type": "text", "width": 100 },
          { "name": "CUT_KNIFE_HEIGHT", "label": "切刀刀高", "type": "text", "width": 100 },
          { "name": "LACING_KNIFE", "label": "撕裂刀", "type": "text", "width": 100 },
          { "name": "LACING_KNIFE_HEIGHT", "label": "撕裂刀刀高", "type": "text", "width": 100 },
          { "name": "CREATE_TIME", "label": "创建时间", "type": "datetime", "width": 150 },
          { "name": "CREATE_BY", "label": "创建人", "type": "text", "width": 100 },
          { "name": "KNIFE_TYPE", "label": "刀具类型", "type": "text", "width": 100 },
          { "name": "KNIFE_LAYOUT", "label": "刀具轨迹布局", "type": "text", "width": 120 },
          { "name": "DP_ZTL", "label": "刀盘总推力", "type": "text", "width": 100 },
          { "name": "DP_NJ", "label": "刀盘扭矩", "type": "text", "width": 100 },
          { "name": "DP_ZS", "label": "刀盘转速", "type": "text", "width": 100 },
          { "name": "DP_GRD", "label": "刀盘贯入度", "type": "text", "width": 100 },
          { "name": "DP_ZJCL", "label": "刀盘总接触力", "type": "text", "width": 100 }
        ]
      }
    ]
  };

  window.jsonpCallback && window.jsonpCallback(response);
})();