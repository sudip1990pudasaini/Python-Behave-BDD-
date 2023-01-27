### Modal ###
modal = {"xpath": "//*[@class='modal-content']"}
modal_title = {"xpath": "//*[@class='modal-content']/div/h3"}
task_description = {"id": "edit_task"}
subtask_description = {"id": "new_sub_task"}
subtask_due_date = {"id": "dueDate"}
add_subtask_button = {"id": "add-subtask"}
modal_close_button = {"xpath": "//*[@class='modal-content']/div[3]/button"}

### Subtasks Table ###
table = "//*[@class = 'modal-content']/div/div[2]/table"
table_title = {"xpath": "//*[@class = 'modal-content']/div/div[2]/h4"}
subtasks_table = {"xpath": "//*[@class = 'modal-content']/div/div[2]/table"}
subtasks_table_first_row = {"xpath": table + "/tbody/tr[1]"}
subtasks_table_first_row_content = {"xpath": table + "/tbody/tr[1]/td[2]/a"}
