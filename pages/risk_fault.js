(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "新增风险与故障记录",
        "icon": "fa fa-plus",
        "level": "primary",
        "className": "m-b-sm",
        "actionType": "dialog",
        "dialog": {
          "title": "新增风险与故障记录",
          "body": {
            "type": "form",
            "api": {
              "method": "post",
              "url": "/risk_fault/risk_fault",
              "messages": {
                "success": "添加成功",
                "failed": "添加失败"
              }
            },
            "body": [
              {"type": "input-text", "name": "connect_key", "label": "盾构机编号", "required": true},
              {"type": "input-number", "name": "ring", "label": "施工环号", "required": true},
              {"type": "input-text", "name": "sub_code", "label": "施工区间编码", "required": true},
              {"type": "input-text", "name": "sub_name", "label": "施工区间名称", "required": true},
              {"type": "input-text", "name": "risk_start_end_ring", "label": "风险源起止环号"},
              {"type": "input-text", "name": "risk_type", "label": "风险类型"},
              {"type": "input-text", "name": "risk_content", "label": "风险源信息"},
              {"type": "input-text", "name": "risk_level", "label": "风险等级"},
              {"type": "input-text", "name": "risk_desc", "label": "风险描述"},
              {"type": "input-text", "name": "risk_prevention", "label": "预防措施"},
              {"type": "input-text", "name": "risk_treatment", "label": "处理方法"},
              {"type": "input-text", "name": "risk_impact", "label": "对工程的影响"},
              {"type": "input-text", "name": "risk_early_warning", "label": "风险预警指标"},
              {"type": "input-text", "name": "risk_early_warning_value", "label": "风险预警值"},
              {"type": "input-text", "name": "risk_monitoring_frequency", "label": "监测频率"},
              {"type": "input-text", "name": "surface_settlement_monitoring_value", "label": "地表沉降监测值"},
              {"type": "input-text", "name": "structure_deformation_value", "label": "建构筑物变形值"},
              {"type": "input-text", "name": "alarm_ring_section", "label": "警报所在环号"},
              {"type": "input-text", "name": "alarm_type", "label": "警报类型"},
              {"type": "input-text", "name": "fault_occurrence_time", "label": "故障发生时间"},
              {"type": "input-text", "name": "specific_fault_equipment", "label": "故障具体设备"},
              {"type": "input-text", "name": "fault_type", "label": "故障类型"},
              {"type": "input-text", "name": "fault_treatment_measures", "label": "故障处理措施"},
              {"type": "input-text", "name": "sg_fssj", "label": "事故发生时间"},
              {"type": "input-text", "name": "sg_yy", "label": "事故原因"},
              {"type": "input-text", "name": "cl_jg", "label": "处理结果"},
              {"type": "input-text", "name": "wx_yy", "label": "维修原因"},
              {"type": "input-text", "name": "wx_nr", "label": "维修内容"}
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
          "url": "/risk_fault/risk_fault_list",
          "method": "get",
          "dataType": "json"
        },
        "headerToolbar": [
          {
            "type": "tpl",
            "tpl": "<div class='header-title'><i class='fa fa-cog'></i> 风险与故障记录管理</div>"
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
            {"type": "input-text", "name": "sub_code", "label": "施工区间编码", "placeholder": "请输入施工区间编码进行查询"},
            {"type": "input-text", "name": "sub_name", "label": "施工区间名称", "placeholder": "请输入施工区间名称进行查询"}
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
                  "title": "修改风险与故障记录",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/risk_fault/update_risk_fault",
                      "messages": {
                        "success": "更新成功",
                        "failed": "更新失败"
                      }
                    },
                    "body": [
                      {"type": "hidden", "name": "id"},
                      {"type": "input-text", "name": "connect_key", "label": "盾构机编号", "required": true},
                      {"type": "input-number", "name": "ring", "label": "施工环号", "required": true},
                      {"type": "input-text", "name": "sub_code", "label": "施工区间编码", "required": true},
                      {"type": "input-text", "name": "sub_name", "label": "施工区间名称", "required": true},
                      {"type": "input-text", "name": "risk_start_end_ring", "label": "风险源起止环号"},
                      {"type": "input-text", "name": "risk_type", "label": "风险类型"},
                      {"type": "input-text", "name": "risk_content", "label": "风险源信息"},
                      {"type": "input-text", "name": "risk_level", "label": "风险等级"},
                      {"type": "input-text", "name": "risk_desc", "label": "风险描述"},
                      {"type": "input-text", "name": "risk_prevention", "label": "预防措施"},
                      {"type": "input-text", "name": "risk_treatment", "label": "处理方法"},
                      {"type": "input-text", "name": "risk_impact", "label": "对工程的影响"},
                      {"type": "input-text", "name": "risk_early_warning", "label": "风险预警指标"},
                      {"type": "input-text", "name": "risk_early_warning_value", "label": "风险预警值"},
                      {"type": "input-text", "name": "risk_monitoring_frequency", "label": "监测频率"},
                      {"type": "input-text", "name": "surface_settlement_monitoring_value", "label": "地表沉降监测值"},
                      {"type": "input-text", "name": "structure_deformation_value", "label": "建构筑物变形值"},
                      {"type": "input-text", "name": "alarm_ring_section", "label": "警报所在环号"},
                      {"type": "input-text", "name": "alarm_type", "label": "警报类型"},
                      {"type": "input-text", "name": "fault_occurrence_time", "label": "故障发生时间"},
                      {"type": "input-text", "name": "specific_fault_equipment", "label": "故障具体设备"},
                      {"type": "input-text", "name": "fault_type", "label": "故障类型"},
                      {"type": "input-text", "name": "fault_treatment_measures", "label": "故障处理措施"},
                      {"type": "input-text", "name": "sg_fssj", "label": "事故发生时间"},
                      {"type": "input-text", "name": "sg_yy", "label": "事故原因"},
                      {"type": "input-text", "name": "cl_jg", "label": "处理结果"},
                      {"type": "input-text", "name": "wx_yy", "label": "维修原因"},
                      {"type": "input-text", "name": "wx_nr", "label": "维修内容"}
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
                  "url": "/risk_fault/delete_risk_fault/${id}"
                },
                "messages": {
                  "success": "删除成功",
                  "failed": "删除失败"
                }
              }
            ]
          },
          { "name": "id", "label": "编号","type": "number", "width": 80 },
          { "name": "connect_key", "label": "盾构机编号", "type": "text", "width": 120 },
          { "name": "ring", "label": "施工环号", "type": "number", "width": 100 },
          { "name": "sub_code", "label": "施工区间编码", "type": "text", "width": 120 },
          { "name": "sub_name", "label": "施工区间名称", "type": "text", "width": 150 },
          { "name": "risk_start_end_ring", "label": "风险源起止环号", "type": "text", "width": 120 },
          { "name": "risk_type", "label": "风险类型", "type": "text", "width": 100 },
          { "name": "risk_content", "label": "风险源信息", "type": "text", "width": 150 },
          { "name": "risk_level", "label": "风险等级", "type": "text", "width": 100 },
          { "name": "risk_desc", "label": "风险描述", "type": "text", "width": 150 },
          { "name": "risk_prevention", "label": "预防措施", "type": "text", "width": 150 },
          { "name": "risk_treatment", "label": "处理方法", "type": "text", "width": 150 },
          { "name": "risk_impact", "label": "对工程的影响", "type": "text", "width": 150 },
          { "name": "risk_early_warning", "label": "风险预警指标", "type": "text", "width": 120 },
          { "name": "risk_early_warning_value", "label": "风险预警值", "type": "text", "width": 120 },
          { "name": "risk_monitoring_frequency", "label": "监测频率", "type": "text", "width": 100 },
          { "name": "surface_settlement_monitoring_value", "label": "地表沉降监测值", "type": "text", "width": 150 },
          { "name": "structure_deformation_value", "label": "建构筑物变形值", "type": "text", "width": 150 },
          { "name": "alarm_ring_section", "label": "警报所在环号", "type": "text", "width": 120 },
          { "name": "alarm_type", "label": "警报类型", "type": "text", "width": 100 },
          { "name": "fault_occurrence_time", "label": "故障发生时间", "type": "text", "width": 150 },
          { "name": "specific_fault_equipment", "label": "故障具体设备", "type": "text", "width": 150 },
          { "name": "fault_type", "label": "故障类型", "type": "text", "width": 100 },
          { "name": "fault_treatment_measures", "label": "故障处理措施", "type": "text", "width": 150 },
          { "name": "sg_fssj", "label": "事故发生时间", "type": "text", "width": 150 },
          { "name": "sg_yy", "label": "事故原因", "type": "text", "width": 150 },
          { "name": "cl_jg", "label": "处理结果", "type": "text", "width": 150 },
          { "name": "wx_yy", "label": "维修原因", "type": "text", "width": 150 },
          { "name": "wx_nr", "label": "维修内容", "type": "text", "width": 150 }
        ]
      }
    ]
  };

  window.jsonpCallback && window.jsonpCallback(response);
})();