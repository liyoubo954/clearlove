(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "crud",
        "syncLocation": false,
        "resizable": true,
        "columnsTogglable": true,
        "className": "table-db m-b-none",
        "tableClassName": "table-cell-nowrap",
        "api": {
          "url": "/daily_paper/daily_paper_list",
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
            "tpl": "<div class='header-title'><i class='fa fa-file-text'></i> 盾构日报表数据</div>"
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
        "exportExcel": {
          "filename": "日报表数据",
          "columns": [
            "id", "areaId", "ljsh", "dpnj", "jjbz", "cjll", "dpzs", "kslc", "qjcd",
            "tjsd", "jjll", "cjbz", "jrjd", "ztl", "qjyl", "grd", "wcd",
            "qkyl", "qpcyl", "qjmc", "dgjbh", "pjrjc", "jslc", "sfsj", "time"
          ]
        },
        "filter": {
          "title": "查询条件",
          "submitText": "查询",
          "body": [
            {
              "type": "input-text",
              "name": "id",
              "label": "编号",
              "placeholder": "请输入编号进行查询"
            },
            {
              "type": "input-text",
              "name": "areaId",
              "label": "盾构机编码id",
              "placeholder": "请输入盾构机编码id进行查询"
            },
            {
              "type": "input-text",
              "name": "qjmc",
              "label": "区间名称",
              "placeholder": "请输入区间名称进行查询"
            },
            {
              "type": "input-text",
              "name": "dgjbh",
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
                  "size": "lg",
                  "title": "修改日报表信息",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/daily_paper/update_daily_paper",
                      "messages": {
                        "success": "更新成功",
                        "failed": "更新失败"
                      }
                    },
                    "body": [
                      {"type": "hidden", "name": "id"},
                      {"type": "input-number", "name": "areaId", "label": "盾构机编码id"},
                      {"type": "input-number", "name": "ljsh", "label": "累积时间"},
                      {"type": "input-text", "name": "dpnj", "label": "刀盘扭矩"},
                      {"type": "input-text", "name": "jjbz", "label": "进尺比重"},
                      {"type": "input-text", "name": "cjll", "label": "出浆流量"},
                      {"type": "input-text", "name": "dpzs", "label": "刀盘转速"},
                      {"type": "input-number", "name": "kslc", "label": "开始里程"},
                      {"type": "input-number", "name": "qjcd", "label": "区间长度"},
                      {"type": "input-text", "name": "tjsd", "label": "推进速度"},
                      {"type": "input-text", "name": "jjll", "label": "进浆流量"},
                      {"type": "input-text", "name": "cjbz", "label": "出浆比重"},
                      {"type": "input-text", "name": "jrjd", "label": "今日进度环"},
                      {"type": "input-text", "name": "ztl", "label": "总推力"},
                      {"type": "input-number", "name": "qjyl", "label": "区间余量"},
                      {"type": "input-text", "name": "grd", "label": "贯入度"},
                      {"type": "input-text", "name": "wcd", "label": "完成度"},
                      {"type": "input-text", "name": "qkyl", "label": "初压力"},
                      {"type": "input-text", "name": "qpcyl", "label": "气泡仓压力"},
                      {"type": "input-text", "name": "qjmc", "label": "区间名称"},
                      {"type": "input-text", "name": "dgjbh", "label": "盾构机编号"},
                      {"type": "input-number", "name": "pjrjc", "label": "平均日进尺"},
                      {"type": "input-number", "name": "jslc", "label": "结束里程"},
                      {"type": "input-text", "name": "sfsj", "label": "始发时间"},
                      {"type": "input-datetime", "name": "time", "label": "日期"}
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
                  "url": "/daily_paper/delete_daily_paper/${id}"
                },
                "messages": {
                  "success": "删除成功",
                  "failed": "删除失败"
                }
              }
            ]
          },
          { "name": "id", "label": "编号", "type": "number", "width": 80 },
          { "name": "areaId", "label": "盾构机编码id", "type": "number", "width": 120 },
          { "name": "ljsh", "label": "累积时间", "type": "number", "width": 100 },
          { "name": "dpnj", "label": "刀盘扭矩", "type": "text", "width": 100 },
          { "name": "jjbz", "label": "进尺比重", "type": "text", "width": 100 },
          { "name": "cjll", "label": "出浆流量", "type": "text", "width": 100 },
          { "name": "dpzs", "label": "刀盘转速", "type": "text", "width": 100 },
          { "name": "kslc", "label": "开始里程", "type": "number", "width": 100 },
          { "name": "qjcd", "label": "区间长度", "type": "number", "width": 100 },
          { "name": "tjsd", "label": "推进速度", "type": "text", "width": 100 },
          { "name": "jjll", "label": "进浆流量", "type": "text", "width": 100 },
          { "name": "cjbz", "label": "出浆比重", "type": "text", "width": 100 },
          { "name": "jrjd", "label": "今日进度环", "type": "text", "width": 100 },
          { "name": "ztl", "label": "总推力", "type": "text", "width": 100 },
          { "name": "qjyl", "label": "区间余量", "type": "number", "width": 100 },
          { "name": "grd", "label": "贯入度", "type": "text", "width": 100 },
          { "name": "wcd", "label": "完成度", "type": "text", "width": 100 },
          { "name": "qkyl", "label": "初压力", "type": "text", "width": 100 },
          { "name": "qpcyl", "label": "气泡仓压力", "type": "text", "width": 100 },
          { "name": "qjmc", "label": "区间名称", "type": "text", "width": 100 },
          { "name": "dgjbh", "label": "盾构机编号", "type": "text", "width": 100 },
          { "name": "pjrjc", "label": "平均日进尺", "type": "number", "width": 100 },
          { "name": "jslc", "label": "结束里程", "type": "number", "width": 100 },
          { "name": "sfsj", "label": "始发时间", "type": "text", "width": 100 },
          { "name": "time", "label": "日期", "type": "date", "width": 120 }
        ],
        "perPage": 10,
        "messages": {
          "fetchFailed": "查询失败，请检查网络或联系管理员"
        },
        "style": {
          "table": {
            "overflow": "auto",
            "maxHeight": "500px"
          }
        },
        "cssVars": {
          "--Table-content-paddingX": "1rem",
          "--Table-thead-height": "2.5rem"
        },
        "css": {
          ".text-ellipsis": {
            "whiteSpace": "nowrap",
            "overflow": "hidden",
            "textOverflow": "ellipsis",
            "maxWidth": "100%"
          },
          ".table-db th": {
            "backgroundColor": "#f5f7fa",
            "fontWeight": "500"
          },
          ".table-db td": {
            "padding": "8px"
          }
        }
      }
    ]
  };

  // 添加自定义样式
  const style = document.createElement('style');
  style.textContent = `
    .text-ellipsis {
      white-space: nowrap !important;
      overflow: hidden !important;
      text-overflow: ellipsis !important;
      max-width: 100% !important;
    }
    .text-nowrap {
      white-space: nowrap !important;
    }
    .table-db {
      border-radius: 4px;
      overflow: hidden;
    }
    .table-db th {
      background-color: #f5f7fa !important;
      font-weight: 500;
    }
    .table-db td {
      max-width: 0 !important;
      padding: 8px !important;
      overflow: hidden !important;
    }
    .table-db .cxd-Table-content {
      overflow: auto !important;
    }
  `;
  document.head.appendChild(style);

  window.jsonpCallback && window.jsonpCallback(response);
})();
