<template>
  <v-container fluid>
    <v-layout row fill-height>
      <v-flex xs5>
        <h2>Tags</h2>
        <v-treeview
          :active.sync="active"
          :items="items"
          activatable
          open-on-click
        >
        </v-treeview>
      </v-flex>
      <v-flex xs7>
        <div v-if="!selectedHTML">Select a Tag</div>
        <div v-else v-html="selectedHTML"></div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { namespace } from 'vuex-class';
import marked from 'marked';
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src

import adrs from '@/store/modules/adrs';
import { Tag, ADR } from '@/store/modules/adrs/types';

interface TagTree {
  id?: number;
  children: { [tagPart: string]: TagTree };
}

@Component({
  components: {
    HelloWorld,
  },
})
export default class Home extends Vue {
  public active: string[] = [];

  private created() {
    adrs.loadADRs();
  }

  get selectedHTML() {
    if (!this.active.length) {
      return undefined;
    }
    const id = Number(this.active[0].split('.').pop());
    const selectedAdr = adrs.adrs.find((adr) => adr.id === id);
    return marked(selectedAdr!.content);
  }

  get items() {
    const root: TagTree = { children: {} };
    const populateNode = (node: TagTree, tag: Tag, adr: ADR) => {
      if (tag.length === 0) {
        node.id = adr.id;
      } else {
        const first = tag[0];
        const rest = tag.splice(1);
        if (!node.children[first]) {
          node.children[first] = { children: {} };
        }
        populateNode(node.children[first], rest, adr);
      }
    };
    adrs.adrs.forEach((adr) => {
      adr.tags.forEach((tag) => {
        populateNode(root, tag, adr);
      });
    });
    const extractChildren = (node: TagTree, prefix: string): any => {
      const children = node.children;
      return Object.keys(children).map((tagPart: string) => {
        const child = children[tagPart];
        const childHasChildren = Object.keys(child.children).length > 0;
        return {
          id: `${prefix}.${tagPart}.${child.id}`,
          name: tagPart,
          children: childHasChildren
            ? extractChildren(child, `${prefix}.${tagPart}`)
            : undefined,
        };
      });
    };
    return extractChildren(root, '');
  }
}
</script>
