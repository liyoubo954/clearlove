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
          "url": "/bar_chart/bar_chart_report",
          "method": "get",
          "dataType": "json"
        },
        // 添加导出按钮和配置
        "headerToolbar": [
          {
            "type": "tpl",
            "tpl": "<div class='header-title'><i class='fa fa-bar-chart'></i> 盾构报表数据</div>"
          },
          "export-excel",
          {
            "type": "columns-toggler",
            "align": "right",
            "icon": "fa fa-list",
            "tooltip": "显示/隐藏列",
            "tooltipPlacement": "top"
          },
          {
            "type": "reload",
            "icon": "fa fa-refresh",
            "tooltip": "刷新数据",
            "tooltipPlacement": "top",
            "level": "link"
          }
        ],
        "exportExcel": {
          "filename": "项目报表数据",
          "columns": [
            "id",
            "sub_code",
            "sub_name",
            "type",
            "connect_key",
            "take_time",
            "time",
            "driver",
            "foreman",
            "assembler",
            "work_time",
            "fault_time"
          ]
        },
        "filter": {
          "title": "查询条件",
          "submitText": "查询",
          "body": [
            {
              "type": "input-text",
              "name": "sub_name",
              "label": "项目名称",
              "placeholder": "输入项目名称"
            },
            {
              "type": "input-text",
              "name": "sub_code",
              "label": "项目编码",
              "placeholder": "输入项目编码"
            },
            {
              "type": "select",
              "name": "type",
              "label": "项目类型",
              "placeholder": "请选择项目类型",
              "clearable": true,
              "options": [
                { "label": "类型1", "value": 1 },
                { "label": "类型2", "value": 2 }
              ]
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
                  "title": "修改项目信息",
                  "body": {
                    "type": "form",
                    "reload": "crud",
                    "api": {
                      "method": "put",
                      "url": "/bar_chart/update_report/${id}",
                      "messages": {
                        "success": "项目信息更新成功"
                      }
                    },
                    "body": [
                      {
                        "type": "hidden",
                        "name": "id"
                      },
                      {
                        "type": "input-text",
                        "name": "sub_name",
                        "label": "项目名称",
                        "required": true
                      },
                      {
                        "type": "input-text",
                        "name": "sub_code",
                        "label": "项目编码",
                        "required": true
                      },
                      {
                        "type": "select",
                        "name": "type",
                        "label": "项目类型",
                        "required": true,
                        "options": [
                          { "label": "类型1", "value": 1 },
                          { "label": "类型2", "value": 2 }
                        ]
                      },
                      {
                        "type": "input-text",
                        "name": "connect_key",
                        "label": "盾构机编号",
                        "required": true
                      },
                      {
                        "type": "input-text",
                        "name": "driver",
                        "label": "驾驶员"
                      },
                      {
                        "type": "input-text",
                        "name": "foreman",
                        "label": "厂长"
                      },
                      {
                        "type": "input-text",
                        "name": "assembler",
                        "label": "装配员"
                      }
                    ]
                  },
                  "actions": [
                    {
                      "type": "button",
                      "label": "取消",
                      "actionType": "close"
                    },
                    {
                      "type": "button",
                      "label": "提交",
                      "actionType": "submit",
                      "level": "primary"
                    }
                  ]
                }
              },
              {
                "type": "button",
                "icon": "fa fa-times text-danger",
                "actionType": "ajax",
                "tooltip": "删除",
                "confirmText": "确定要删除该项目吗？删除后数据将无法恢复！",
                "api": "/bar_chart/delete_report/${id}",
                "messages": {
                  "success": "删除成功",
                  "failed": "删除失败"
                },
                "reload": "crud"
              }
            ]
          },
          { "name": "id", "label": "编号", "type": "text", "width": 80 },
          { "name": "sub_code", "label": "项目编码", "type": "text", "resizable": true, "width": 120, "classNameBody": "text-ellipsis text-nowrap" },
          { "name": "sub_name", "label": "项目名称", "type": "text", "resizable": true, "width": 150, "classNameBody": "text-ellipsis text-nowrap" },
          {
            "name": "type",
            "label": "项目类型",
            "type": "mapping",
            "width": 100,
            "map": {
              "1": "类型1",
              "2": "类型2"
            }
          },
          { "name": "connect_key", "label": "盾构机编号", "type": "text", "resizable": true, "width": 200, "classNameBody": "text-ellipsis text-nowrap" },
          { "name": "take_time", "label": "耗时", "type": "text", "width": 100 },
          {
            "name": "time",
            "label": "时间戳",
            "type": "date",
            "format": "YYYY-MM-DD HH:mm:ss",
            "width": 160,
            "resizable": true
          },
          { "name": "driver", "label": "驾驶员", "type": "text", "resizable": true, "width": 100, "classNameBody": "text-ellipsis text-nowrap" },
          { "name": "foreman", "label": "厂长", "type": "text", "resizable": true, "width": 100, "classNameBody": "text-ellipsis text-nowrap" },
          { "name": "assembler", "label": "装配工", "type": "text", "resizable": true, "width": 100, "classNameBody": "text-ellipsis text-nowrap" },
          {
            "name": "work_time",
            "label": "工作时间",
            "type": "text",
            "width": 300,
            "resizable": true,
            "classNameBody": "text-ellipsis text-nowrap",
            "render": function (value) {
              return this.renderShortData(value);
            }
          },
          {
            "name": "fault_time",
            "label": "故障时间",
            "type": "text",
            "width": 300,
            "resizable": true,
            "classNameBody": "text-ellipsis text-nowrap",
            "render": function (value) {
              return this.renderShortData(value);
            }
          }
        ],
        "perPage": 10,
        "messages": {
          "fetchFailed": "查询失败，请检查权限或联系管理员"
        },

        "methods": {
          renderShortData(value) {
            if (!value) return "无数据";
            if (typeof value === 'string') {
              return value.length > 50 ? value.substr(0, 50) + '...' : value;
            }
            if (typeof value === 'object') {
              return JSON.stringify(value).substr(0, 50) + '...';
            }
            return value;
          },

        },
        "style": {
          "table": {
            "overflow": "auto",
            "maxHeight": "500px"
          },

        },
        "columnsTogglable": false,
        "cssVars": {
          "--Table-content-paddingX": "1rem",
          "--Table-thead-height": "2.5rem",
          "--Table-action-space": "0.25rem"
        },
        "css": {
          ".cxd-Button--size-xs": {
            "padding": "2px 8px",
            "fontSize": "12px",
            "borderRadius": "2px",
            "background": "transparent"
          },
          ".cxd-Button--size-xs:hover": {
            "background": "#f0f0f0"
          },
          ".text-primary": {
            "color": "#1976D2 !important"
          },
          ".text-danger": {
            "color": "#D32F2F !important"
          },
          ".cxd-Table-content": {
            "overflow": "visible"
          },
          ".cxd-Table-table > tbody > tr > td.cxd-Table-operationCell": {
            "minWidth": "80px",
            "padding": "0.5rem"
          },
          ".cxd-Table-table > tbody > tr > td.cxd-Table-operationCell .cxd-Button": {
            "margin": "0 0.25rem"
          },
          ".header-title": {
            "fontSize": "1.2rem",
            "fontWeight": "bold",
            "color": "#333",
            "margin": "0.5rem 0"
          },
          ".header-title i": {
            "marginRight": "0.5rem",
            "color": "#4c51bf"
          },
          ".cxd-Table-table > thead > tr > th": {
            "backgroundColor": "#f8f9fa",
            "fontWeight": "600",
            "color": "#333"
          },
          ".cxd-Table-table > tbody > tr:hover": {
            "backgroundColor": "#f0f4f8"
          },
          ".cxd-Table-table": {
            "border": "1px solid #eee",
            "borderRadius": "4px",
            "overflow": "hidden"
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
