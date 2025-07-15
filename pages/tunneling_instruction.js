(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "新增盾构掘进指令",
        "icon": "fa fa-plus",
        "level": "primary",
        "className": "m-b-sm",
        "actionType": "dialog",
        "dialog": {
          "title": "新增盾构掘进指令",
          "body": {
            "type": "form",
            "api": {
              "method": "post",
              "url": "/tunneling_instruction/tunneling_instruction",
              "messages": {
                "success": "添加成功",
                "failed": "添加失败"
              }
            },
            "body": [
              {
                "type": "input-text",
                "name": "project_code",
                "label": "盾构机编号",
                "required": true
              },
              {
                "type": "input-text",
                "name": "project_name",
                "label": "项目名称",
                "required": true
              },
              {
                "type": "input-number",
                "name": "ring_number",
                "label": "环号"
              },
              {
                "type": "input-text",
                "name": "cutting_face_mileage",
                "label": "切口里程"
              },
              {
                "type": "input-number",
                "name": "cover_thickness",
                "label": "覆土厚度 (m)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "notch_water_pressure",
                "label": "切口水压 (bar)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-text",
                "name": "total_thrust",
                "label": "总推力 (KN)"
              },
              {
                "type": "input-text",
                "name": "total_torque",
                "label": "总扭矩 (MN·m)"
              },
              {
                "type": "input-text",
                "name": "tunneling_speed",
                "label": "掘进速度 (mm/min)"
              },
              {
                "type": "input-number",
                "name": "cutterhead_speed",
                "label": "刀盘转速 (rpm)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-text",
                "name": "slurry_ratio",
                "label": "进/排浆比重 (g/cm³)"
              },
              {
                "type": "input-text",
                "name": "slurry_flow",
                "label": "进/排浆流量 (m³/h)"
              },
              {
                "type": "input-number",
                "name": "sync_grouting_pressure_1",
                "label": "同步注浆压力1#(bar)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "sync_grouting_volume_1",
                "label": "同步注浆量1#(m³)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "sync_grouting_pressure_2",
                "label": "同步注浆压力2#(bar)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "sync_grouting_volume_2",
                "label": "同步注浆量2#(m³)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "sync_grouting_pressure_3",
                "label": "同步注浆压力3#(bar)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "sync_grouting_volume_3",
                "label": "同步注浆量3#(m³)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "sync_grouting_pressure_4",
                "label": "同步注浆压力4#(bar)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "sync_grouting_volume_4",
                "label": "同步注浆量4#(m³)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "sync_grouting_pressure_5",
                "label": "同步注浆压力5#(bar)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "sync_grouting_volume_5",
                "label": "同步注浆量5#(m³)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "sync_grouting_pressure_6",
                "label": "同步注浆压力6#(bar)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-number",
                "name": "sync_grouting_volume_6",
                "label": "同步注浆量6#(m³)",
                "step": 0.01,
                "precision": 2
              },
              {
                "type": "input-text",
                "name": "excel_path",
                "label": "上传excel路径"
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
          "url": "/tunneling_instruction/tunneling_instruction_list",
          "method": "get",
          "dataType": "json"
        },
        "headerToolbar": [
          {
            "type": "tpl",
            "tpl": "<div class='header-title'><i class='fa fa-cog'></i> 盾构掘进指令表</div>"
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
              "name": "project_code",
              "label": "盾构机编号",
              "placeholder": "请输入盾构机编号进行查询"
            },
            {
              "type": "input-text",
              "name": "project_name",
              "label": "项目名称",
              "placeholder": "请输入项目名称进行查询"
            },
            {
              "type": "input-number",
              "name": "ring_number",
              "label": "环号",
              "placeholder": "请输入环号进行查询"
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
                  "title": "修改盾构掘进指令",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/tunneling_instruction/update_tunneling_instruction",
                      "messages": {
                        "success": "更新成功",
                        "failed": "更新失败"
                      }
                    },
                    "body": [
                      {"type": "hidden", "name": "id"},
                      {"type": "input-text", "name": "project_code", "label": "盾构机编号", "required": true},
                      {"type": "input-text", "name": "project_name", "label": "项目名称", "required": true},
                      {"type": "input-number", "name": "ring_number", "label": "环号"},
                      {"type": "input-text", "name": "cutting_face_mileage", "label": "切口里程"},
                      {"type": "input-number", "name": "cover_thickness", "label": "覆土厚度 (m)", "step": 0.01, "precision": 2},
                      {"type": "input-number", "name": "notch_water_pressure", "label": "切口水压 (bar)", "step": 0.01, "precision": 2},
                      {"type": "input-text", "name": "total_thrust", "label": "总推力 (KN)"},
                      {"type": "input-text", "name": "total_torque", "label": "总扭矩 (MN·m)"},
                      {"type": "input-text", "name": "tunneling_speed", "label": "掘进速度 (mm/min)"},
                      {"type": "input-number", "name": "cutterhead_speed", "label": "刀盘转速 (rpm)", "step": 0.01, "precision": 2},
                      {"type": "input-text", "name": "slurry_ratio", "label": "进/排浆比重 (g/cm³)"},
                      {"type": "input-text", "name": "slurry_flow", "label": "进/排浆流量 (m³/h)"},
                      {"type": "input-number", "name": "sync_grouting_pressure_1", "label": "同步注浆压力1#(bar)"},
                      {"type": "input-number", "name": "sync_grouting_volume_1", "label": "同步注浆量1#(m³)"},
                      {"type": "input-number", "name": "sync_grouting_pressure_2", "label": "同步注浆压力2#(bar)"},
                      {"type": "input-number", "name": "sync_grouting_volume_2", "label": "同步注浆量2#(m³)"},
                      {"type": "input-number", "name": "sync_grouting_pressure_3", "label": "同步注浆压力3#(bar)"},
                      {"type": "input-number", "name": "sync_grouting_volume_3", "label": "同步注浆量3#(m³)"},
                      {"type": "input-number", "name": "sync_grouting_pressure_4", "label": "同步注浆压力4#(bar)"},
                      {"type": "input-number", "name": "sync_grouting_volume_4", "label": "同步注浆量4#(m³)"},
                      {"type": "input-number", "name": "sync_grouting_pressure_5", "label": "同步注浆压力5#(bar)"},
                      {"type": "input-number", "name": "sync_grouting_volume_5", "label": "同步注浆量5#(m³)"},
                      {"type": "input-number", "name": "sync_grouting_pressure_6", "label": "同步注浆压力6#(bar)"},
                      {"type": "input-number", "name": "sync_grouting_volume_6", "label": "同步注浆量6#(m³)"},
                      {"type": "input-text", "name": "excel_path", "label": "上传excel路径"}
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
                  "url": "/tunneling_instruction/delete_tunneling_instruction/${id}"
                },
                "messages": {
                  "success": "删除成功",
                  "failed": "删除失败"
                }
              }
            ]
          },
          { "name": "id", "label": "编号", "type": "number", "width": 80 },
          { "name": "project_code", "label": "盾构机编号", "type": "text", "width": 120 },
          { "name": "project_name", "label": "项目名称", "type": "text", "width": 120 },
          { "name": "ring_number", "label": "环号", "type": "number", "width": 80 },
          { "name": "cutting_face_mileage", "label": "切口里程", "type": "text", "width": 120 },
          { "name": "cover_thickness", "label": "覆土厚度 (m)", "type": "number", "width": 120, "precision": 2 },
          { "name": "notch_water_pressure", "label": "切口水压 (bar)", "type": "number", "width": 120, "precision": 2 },
          { "name": "total_thrust", "label": "总推力 (KN)", "type": "text", "width": 120 },
          { "name": "total_torque", "label": "总扭矩 (MN·m)", "type": "text", "width": 120 },
          { "name": "tunneling_speed", "label": "掘进速度 (mm/min)", "type": "text", "width": 120 },
          { "name": "cutterhead_speed", "label": "刀盘转速 (rpm)", "type": "number", "width": 120, "precision": 2 },
          { "name": "slurry_ratio", "label": "进/排浆比重 (g/cm³)", "type": "text", "width": 120 },
          { "name": "slurry_flow", "label": "进/排浆流量 (m³/h)", "type": "text", "width": 120 },
          { "name": "sync_grouting_pressure_1", "label": "同步注浆压力1#(bar)", "type": "number", "width": 150, "precision": 2 },
          { "name": "sync_grouting_volume_1", "label": "同步注浆量1#(m³)", "type": "number", "width": 150, "precision": 2 },
          { "name": "sync_grouting_pressure_2", "label": "同步注浆压力2#(bar)", "type": "number", "width": 150, "precision": 2 },
          { "name": "sync_grouting_volume_2", "label": "同步注浆量2#(m³)", "type": "number", "width": 150, "precision": 2 },
          { "name": "sync_grouting_pressure_3", "label": "同步注浆压力3#(bar)", "type": "number", "width": 150, "precision": 2 },
          { "name": "sync_grouting_volume_3", "label": "同步注浆量3#(m³)", "type": "number", "width": 150, "precision": 2 },
          { "name": "sync_grouting_pressure_4", "label": "同步注浆压力4#(bar)", "type": "number", "width": 150, "precision": 2 },
          { "name": "sync_grouting_volume_4", "label": "同步注浆量4#(m³)", "type": "number", "width": 150, "precision": 2 },
          { "name": "sync_grouting_pressure_5", "label": "同步注浆压力5#(bar)", "type": "number", "width": 150, "precision": 2 },
          { "name": "sync_grouting_volume_5", "label": "同步注浆量5#(m³)", "type": "number", "width": 150, "precision": 2 },
          { "name": "sync_grouting_pressure_6", "label": "同步注浆压力6#(bar)", "type": "number", "width": 150, "precision": 2 },
          { "name": "sync_grouting_volume_6", "label": "同步注浆量6#(m³)", "type": "number", "width": 150, "precision": 2 },
          { "name": "create_time", "label": "创建时间", "type": "datetime", "width": 150 },
          { "name": "update_time", "label": "更新时间", "type": "datetime", "width": 150 },
          { "name": "excel_path", "label": "上传excel路径", "type": "text", "width": 200 }
        ]
      }
    ]
  };

  window.jsonpCallback && window.jsonpCallback(response);
})();