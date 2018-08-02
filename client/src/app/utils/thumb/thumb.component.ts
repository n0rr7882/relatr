import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-thumb',
  templateUrl: './thumb.component.html',
  styleUrls: ['./thumb.component.css']
})
export class ThumbComponent {

  @Input() imagePath: string;

  thumbStyle() {
    return this.imagePath ? { 'background-image': `url(${this.imagePath})` } : null;
  }

}
