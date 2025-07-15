(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "新增管片信息",
        "icon": "fa fa-plus",
        "level": "primary",
        "className": "m-b-sm",
        "actionType": "dialog",
        "dialog": {
          "title": "新增管片信息",
          "body": {
            "type": "form",
            "api": {
              "method": "post",
              "url": "/segment_info/segment_info",
              "messages": {
                "success": "添加成功",
                "failed": "添加失败"
              }
            },
            "body": [
              {
                "type": "input-text",
                "name": "connect_key",
                "label": "盾构机编号",
                "required": true
              },
              {
                "type": "input-number",
                "name": "ring",
                "label": "对应环号",
                "required": true
              },
              {
                "type": "input-text",
                "name": "sub_code",
                "label": "施工区间编码",
                "required": true
              },
              {
                "type": "input-text",
                "name": "sub_name",
                "label": "施工区间名称",
                "required": true
              },
              {
                "type": "input-text",
                "name": "gp_nj",
                "label": "管片内径"
              },
              {
                "type": "input-text",
                "name": "gp_wj",
                "label": "管片外径"
              },
              {
                "type": "input-text",
                "name": "gp_kd",
                "label": "管片宽度"
              },
              {
                "type": "input-text",
                "name": "gp_fks",
                "label": "管片分块数"
              },
              {
                "type": "input-text",
                "name": "dw_sppc",
                "label": "盾尾水平偏差"
              },
              {
                "type": "input-text",
                "name": "ds_szpc",
                "label": "盾尾竖直偏差"
              },
              {
                "type": "input-text",
                "name": "gdj",
                "label": "滚动角"
              },
              {
                "type": "input-text",
                "name": "dg_dta",
                "label": "盾构设计曲线DTA"
              },
              {
                "type": "input-text",
                "name": "gp_pjdw",
                "label": "管片拼接点位"
              },
              {
                "type": "input-text",
                "name": "gp_cql",
                "label": "管片超前量"
              },
              {
                "type": "input-text",
                "name": "gp_zt",
                "label": "管片姿态"
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
          "url": "/segment_info/segment_info_list",
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
            "tpl": "<div class='header-title'><i class='fa fa-cog'></i> 管片信息管理</div>"
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
              "name": "connect_key",
              "label": "盾构机编号",
              "placeholder": "请输入盾构机编号进行查询"
            },
            {
              "type": "input-text",
              "name": "sub_code",
              "label": "施工区间编码",
              "placeholder": "请输入施工区间编码进行查询"
            },
            {
              "type": "input-text",
              "name": "sub_name",
              "label": "施工区间名称",
              "placeholder": "请输入施工区间名称进行查询"
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
                  "title": "修改管片信息",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/segment_info/update_segment_info",
                      "messages": {
                        "success": "更新成功",
                        "failed": "更新失败"
                      }
                    },
                    "body": [
                      {"type": "hidden", "name": "id"},
                      {"type": "input-text", "name": "connect_key", "label": "盾构机编号", "required": true},
                      {"type": "input-number", "name": "ring", "label": "对应环号", "required": true},
                      {"type": "input-text", "name": "sub_code", "label": "施工区间编码", "required": true},
                      {"type": "input-text", "name": "sub_name", "label": "施工区间名称", "required": true},
                      {"type": "input-text", "name": "gp_nj", "label": "管片内径"},
                      {"type": "input-text", "name": "gp_wj", "label": "管片外径"},
                      {"type": "input-text", "name": "gp_kd", "label": "管片宽度"},
                      {"type": "input-text", "name": "gp_fks", "label": "管片分块数"},
                      {"type": "input-text", "name": "dw_sppc", "label": "盾尾水平偏差"},
                      {"type": "input-text", "name": "ds_szpc", "label": "盾尾竖直偏差"},
                      {"type": "input-text", "name": "gdj", "label": "滚动角"},
                      {"type": "input-text", "name": "dg_dta", "label": "盾构设计曲线DTA"},
                      {"type": "input-text", "name": "gp_pjdw", "label": "管片拼接点位"},
                      {"type": "input-text", "name": "gp_cql", "label": "管片超前量"},
                      {"type": "input-text", "name": "gp_zt", "label": "管片姿态"}
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
                  "url": "/segment_info/delete_segment_info/${id}"
                },
                "messages": {
                  "success": "删除成功",
                  "failed": "删除失败"
                }
              }
            ]
          },
          { "name": "id","label": "编号","type": "number", "width": 80 },
          { "name": "connect_key", "label": "盾构机编号", "type": "text", "width": 120 },
          { "name": "ring", "label": "对应环号", "type": "number", "width": 100 },
          { "name": "sub_code", "label": "施工区间编码", "type": "text", "width": 120 },
          { "name": "sub_name", "label": "施工区间名称", "type": "text", "width": 150 },
          { "name": "gp_nj", "label": "管片内径", "type": "text", "width": 100 },
          { "name": "gp_wj", "label": "管片外径", "type": "text", "width": 100 },
          { "name": "gp_kd", "label": "管片宽度", "type": "text", "width": 100 },
          { "name": "gp_fks", "label": "管片分块数", "type": "text", "width": 100 },
          { "name": "dw_sppc", "label": "盾尾水平偏差", "type": "text", "width": 120 },
          { "name": "ds_szpc", "label": "盾尾竖直偏差", "type": "text", "width": 120 },
          { "name": "gdj", "label": "滚动角", "type": "text", "width": 100 },
          { "name": "dg_dta", "label": "盾构设计曲线DTA", "type": "text", "width": 150 },
          { "name": "gp_pjdw", "label": "管片拼接点位", "type": "text", "width": 120 },
          { "name": "gp_cql", "label": "管片超前量", "type": "text", "width": 100 },
          { "name": "gp_zt", "label": "管片姿态", "type": "text", "width": 100 }
        ]
      }
    ]
  };
   window.jsonpCallback && window.jsonpCallback(response);
})();