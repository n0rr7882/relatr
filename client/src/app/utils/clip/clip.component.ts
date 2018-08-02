import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-clip',
  templateUrl: './clip.component.html',
  styleUrls: ['./clip.component.css']
})
export class ClipComponent {

  @Input() imagePath: string;
  @Input() title: string;
  @Input() description: string;

}
