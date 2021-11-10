import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page {

  items: Array<any>;

  constructor(
    public api: ApiService
  ){

  }

  loadData(){
    this.api.getItems().subscribe(res => {
      console.log(res);
      this.items = res;
    }, err => {
      console.error(err);
    });
  }

  clear(){
    this.items = [];
  }
}
